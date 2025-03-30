from bs4 import BeautifulSoup
import numpy as np
import requests


def scrape_news_titles_and_links(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
    r = requests.get(url, headers=headers)
    
    # Parsuj stronę za pomocą BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    print (soup)
    # Znajdź wszystkie elementy <h2> z klasą 'is-title post-title'
    articles = soup.find_all('h2', class_='is-title post-title', limit=6)
    
    # Iteruj przez znalezione elementy i wyodrębnij tytuł i link
    for article in articles:
        title = article.get_text(strip=True)
        link = article.find('a')['href']
        print(f"Tytuł: {title}")
        print(f"Link: {link}\n")
