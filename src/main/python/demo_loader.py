import psycopg2
from bs4 import BeautifulSoup
from datetime import datetime

with open('test.xml', 'r', encoding='utf-8') as f:
    data = f.read()
feed = BeautifulSoup(data, "xml")

class article:
    def __init__(self, title, image, content, source, date):
        self.title = title
        self.content = content
        self.image = image
        self.source = source
        self.date = datetime.fromisoformat(date.replace('Z', '+00:00'))

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "date": self.date
        }

articles = []

for item in feed.find_all('artykul'):
    articles.append(article(item.title.text, item.img.text, item.content.text, item.source.text, item.published.text))

conn = psycopg2.connect(
            dbname="terrabase",
            user="admin",
            password="password",
            host="localhost",
        )
curr = conn.cursor()

for article in articles:
    curr.execute(
        "INSERT INTO articles (title, content, image, source, date) VALUES (%s, %s, %s, %s, %s)",
        (article.title, article.content, article.image, article.source, article.date)
    )
    conn.commit()

curr.close()
conn.close()
print(f"Finished inserting {len(articles)} articles.")