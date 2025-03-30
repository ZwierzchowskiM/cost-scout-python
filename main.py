
import schedule
import time
from src.tracker import scrape_news_titles_and_links
from src.email_sender import send_email

def job():
    url = "https://bedroomproducersblog.com/"
    articles = scrape_news_titles_and_links(url)

    recipient_email = 'mzwierzchowski.chatgpt@gmail.com'
    send_email('Daily News Update', articles, recipient_email)

def main():
   
    schedule.every().day.at("05:30").do(job)
    #schedule.every(1).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()