from datetime import datetime
import json

import feedparser
import requests
from bs4 import BeautifulSoup

class article:
    def __init__(self, title, content, source, date):
        self.title = title
        self.content = content
        self.source = source
        self.date = datetime.strptime(date.split(", ")[1], "%m/%d/%Y - %H:%M").isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "date": self.date
        }
url = "https://pap-mediaroom.pl/rss.xml"
feed = feedparser.parse(url).entries
articles = []
print(feed)
for item in feed:
    articles.append(article(item["title"], item["summary"], item["links"][0]["href"], item["published"]))
articles_json = [a.to_dict() for a in articles]
print(articles_json)
respone = requests.post("http://localhost:8080/addBatch", json=articles_json)
print(respone)