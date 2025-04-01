
import schedule
import time
import requests 
from src.tracker import scrape_news_titles_and_links
from src.email_sender import send_email
import threading
from src.app import app 

def start_flask():
    app.run(host='0.0.0.0', port=8000)

def job():
    url = "https://bedroomproducersblog.com/"
    articles = scrape_news_titles_and_links(url)

    recipient_email = 'mazvi.music@gmail.com'
    send_email('Daily News Update', articles, recipient_email)

def check_app_status():

    response = requests.get("http://localhost:8000/ping")
    if response.status_code == 200:
        print("App status: OK")
    else:
        print(f"Unexpected status code: {response.status_code}")



def main():
    
    print("App start")
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()


    schedule.every().day.at("05:30").do(job)
    schedule.every(2).minutes.do(check_app_status)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()