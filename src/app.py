from flask import Flask, jsonify
from src.tracker import scrape_news_titles_and_links
from src.email_sender import send_email


app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'OK'}), 200

def start_flask():
# Funkcja która uruchamia serwer Flask
    app.run(host='0.0.0.0', port=8000)

@app.route('/run-job', methods=['GET'])
def run_job():
    url = "https://bedroomproducersblog.com/"
    articles = scrape_news_titles_and_links(url)
    recipient_email = 'mzwierzchowski.chatgpt@gmail.com'
    send_email('Daily News Update', articles, recipient_email)
    return jsonify({'status': 'Job executed successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)