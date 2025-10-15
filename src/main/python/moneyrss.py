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

        # Ta logika działa idealnie dla formatu daty z money.pl
        parsed_date_naive = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
        dt_utc = parsed_date_naive.replace(tzinfo=ZoneInfo("UTC"))
        dt_poland = dt_utc.astimezone(ZoneInfo("Europe/Warsaw"))

        # Wysyłamy datę bez strefy czasowej, zgodnie z wymaganiami serwera
        self.date = dt_poland.strftime('%Y-%m-%dT%H:%M:%S')

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "source": self.source,
            "date": self.date
        }


# ZMIANA: Adres URL kanału RSS dla money.pl
url = "https://www.money.pl/rss/wiadomosci.xml"

feed = feedparser.parse(url).entries
articles = []

for item in feed:
    # W `item.published` jest data np. "Wed, 15 Oct 2025 12:15:00 +0200"
    articles.append(article(item.title, item.summary, item.link, item.published))

articles_json = [a.to_dict() for a in articles]
print(json.dumps(articles_json, indent=2, ensure_ascii=False))

response = requests.post("http://localhost:8080/addBatch", json=articles_json)
print(response)