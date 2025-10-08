import re

import requests
from bs4 import BeautifulSoup
import json

def get_article(base, url):
    response = requests.get(
        base + url,
        headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    n_str = ""
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        n_str = str(n_str) + str(paragraph.get_text(strip=True))
    n_str = n_str.split("(PAP Biznes)")[0]
    return n_str


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

class article:
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

base = "https://biznes.pap.pl"

response = requests.get(base, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
anchors = soup.find_all('ul', class_='newsList')
articles = []

for anchor in anchors:
    title_tag = anchor.find('h3', class_='title')
    link_tag = None
    if title_tag:
        link_tag = title_tag.find_parent('a', href=True)
        if link_tag and link_tag['href'].startswith('/wiadomosci'):
            articles.append(article(title_tag.text, link_tag.get('href'), get_article(base, link_tag.get('href'))))

for article in articles:
    # print(article.title)
    # print(article.url)
    # print(article.content)
    print(len(article.content))