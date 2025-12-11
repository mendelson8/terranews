import time
import os
import psycopg2
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

MODEL_NAME = 'sdadas/mmlw-retrieval-roberta-large-v2'
model = SentenceTransformer(MODEL_NAME)

BATCH_SIZE = 1
SLEEP_INTERVAL = 60
SIMILARITY_THRESHOLD = 0.80

while True:
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="terrabase",
            user="admin",
            password="password",
            host="localhost",
        )
        cur = conn.cursor()

        cur.execute("SELECT id, title, content FROM articles WHERE cluster_id IS NULL LIMIT %s", (BATCH_SIZE,))
        articles_to_process = cur.fetchall()

        if articles_to_process:
            for article_id, title, raw_content in articles_to_process:
                print(f"Przetwarzam artykuł o ID: {article_id}")

                soup = BeautifulSoup(raw_content, 'html.parser')
                full_text = title + " " + soup.get_text(separator=' ', strip=True)
                vector = model.encode(full_text)


                cur.execute(
                    """
                    SELECT cluster_id FROM articles
                    WHERE content_vector IS NOT NULL AND 1 - (content_vector <=> %s::vector) > %s
                    ORDER BY content_vector <=> %s::vector
                    LIMIT 1;
                    """,
                    (str(vector.tolist()), SIMILARITY_THRESHOLD, str(vector.tolist()))
                )
                matching_cluster = cur.fetchone()

                cluster_to_assign = None
                if matching_cluster:
                    cluster_to_assign = matching_cluster[0]
                    print(f"Znaleziono pasujący klaster: {cluster_to_assign}")
                else:
                    cluster_to_assign = article_id
                    print(f"Tworzę nowy klaster o ID: {cluster_to_assign}")

                cur.execute(
                    """
                    UPDATE articles
                    SET content_vector = %s::vector,
                        cluster_id = %s
                    WHERE id = %s
                    """,
                    (str(vector.tolist()), cluster_to_assign, article_id)
                )
            conn.commit()
            print("Pomyślnie zaktualizowano artykuł.")
        else:
            print(f"Brak nowych artykułów do przypisania. Czekam {SLEEP_INTERVAL} sekund...")
            time.sleep(SLEEP_INTERVAL)

    except psycopg2.Error as e:
        print(f"Błąd bazy danych: {e}")
        if conn:
            conn.rollback()
        time.sleep(SLEEP_INTERVAL)
    finally:
        if conn:
            cur.close()
            conn.close()
