import time
import os
import psycopg2
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from torch.cuda import utilization

MODEL_NAME = 'sdadas/mmlw-retrieval-roberta-large-v2'
model = SentenceTransformer(MODEL_NAME)

BATCH_SIZE = 1
SLEEP_INTERVAL = 60

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

        cur.execute("SELECT id, content FROM articles WHERE content_vector IS NULL LIMIT %s", (BATCH_SIZE,))
        articles_to_process = cur.fetchall()
        if articles_to_process:
            print("znaleziono artykul")
            for article_id, raw_content in articles_to_process:
                soup = BeautifulSoup(raw_content, 'html.parser')
                cleaned_text = soup.get_text(separator=' ', strip=True)

                vector = model.encode(cleaned_text)

                cur.execute(
                    """
                    SELECT cluster_id
                    FROM articles
                    WHERE 1 - (content_vector <=> %s::vector) > %s
                    ORDER BY content_vector <=> %s::vector
                        LIMIT 1;
                    """,
                    (str(vector.tolist()), 85, str(vector.tolist()))
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
                    SET content_vector  = %s,
                        cluster_id      = %s
                    WHERE id = %s
                    """,
                    (vector.tolist(), cluster_to_assign, article_id)
                )
            conn.commit()
            print("udalo sie zaktualizowac artykul")
        else:
            print("Brak nowych artykułów. Czekam...")
            time.sleep(SLEEP_INTERVAL)

    except psycopg2.Error as e:
        print(f"Błąd bazy danych: {e}")
        time.sleep(SLEEP_INTERVAL)
    finally:
        if conn:
            cur.close()
            conn.close()

