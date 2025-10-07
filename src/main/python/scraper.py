import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
class article:
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

response = requests.get("https://www.rp.pl/wydarzenia/kraj/polityka", headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
anchors = soup.find_all('a', class_="contentLink")

articles = []
for anchor in anchors:
    if len(anchor.text) >=10:
        articles.append(article(anchor.get_text(strip=True), anchor.get('href'), "123"))

for article in articles:
    print(article.title)
    print(article.url)
    print(article.content)