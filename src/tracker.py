from bs4 import BeautifulSoup
import requests
from src.models import Article


def scrape_news_titles_and_links(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()  
    except requests.RequestException as e:
        print(f"Błąd pobierania strony: {e}")
        return []

    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article', class_='l-post grid-post grid-base-post', limit=6)
    
    results = []
    for article in articles:
        title_tag = article.find('h2', class_='is-title post-title')
        title = title_tag.get_text(strip=True)
        link = title_tag.find('a')['href']
        date_tag = article.find('time', class_='post-date')
        date = date_tag.get_text(strip=True) if date_tag else 'Brak daty'
        results.append(Article(title, link, date))
    return results