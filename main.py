# main.py

from src.tracker import scrape_news_titles_and_links
from src.email_sender import send_email

LINK = "https://bedroomproducersblog.com/"

def main():

    url = "https://bedroomproducersblog.com/"
    articles = scrape_news_titles_and_links(url)

    # Adres e-mail odbiorcy
    recipient_email = 'mzwierzchowski.chatgpt@gmail.com'

    # Wyślij e-mail z wynikami
    send_email('Daily News Update', articles, recipient_email)

if __name__ == "__main__":
    main()