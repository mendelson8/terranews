from datetime import datetime
import json
from zoneinfo import ZoneInfo

import feedparser
import requests


class article:
    def __init__(self, title, content, source, date):
        self.title = title
        self.content = content
        self.source = source

        parsed_date_naive = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
        dt_utc = parsed_date_naive.replace(tzinfo=ZoneInfo("UTC"))
        dt_poland = dt_utc.astimezone(ZoneInfo("Europe/Warsaw"))
        self.date = dt_poland.strftime('%Y-%m-%dT%H:%M:%S')

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "date": self.date
        }


url = "https://wyborcza.pl/pub/rss/najnowsze_wyborcza.xml"
feed = feedparser.parse(url).entries
articles = []

for item in feed:
    articles.append(article(item.title, item.summary, item.link, item.published))

articles_json = [a.to_dict() for a in articles]
print(json.dumps(articles_json, indent=2, ensure_ascii=False))

response = requests.post("http://localhost:8080/addBatch", json=articles_json)
print(response)