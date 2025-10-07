import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


response = requests.get("https://www.rp.pl/wydarzenia/kraj/polityka", headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
a_tags = soup.find_all("a", class_="contentLink")

articles = []

for a in a_tags:
    h2 = a.find("h2")
    if h2:
        title = h2.get_text(strip=True)
        link = a.get("href")
        articles.append({"title": title, "link": link})

for art in articles:
    print(art["title"], "|", art["link"])

