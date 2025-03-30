# main.py

from src.tracker import scrape_news_titles_and_links

LINK = "https://bedroomproducersblog.com/"

if __name__ == "__main__":
    scrape_news_titles_and_links(LINK)