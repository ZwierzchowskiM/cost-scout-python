import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

def authenticate_gmail():
    # Pobierz dane uwierzytelniające z zmiennych środowiskowych
    


    load_dotenv()  # Wczytaj zmienne z .env

    client_id = os.getenv("GOOGLE_OAUTH2_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_OAUTH2_CLIENT_SECRET")
    refresh_token = os.getenv("GOOGLE_OAUTH2_REFRESH_TOKEN")

   # print(client_id)
   # print(client_secret)
   # print(refresh_token)

    # Utwórz obiekt Credentials
    creds = Credentials.from_authorized_user_info(
        info={
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token,
            'token': '',  # Pusty token, ponieważ używamy refresh token
        },
        #scopes=['https://www.googleapis.com/auth/gmail.modify']
    )

    # Odśwież token, jeśli jest to konieczne
    if creds.expired or not creds.valid:
        creds.refresh(Request())

    return creds

def send_email(subject, articles, to_email):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    # Utwórz wiadomość e-mail
    msg = MIMEMultipart()
    msg['From'] = 'me'
    msg['To'] = to_email
    msg['Subject'] = subject

    # Konwertuj listę obiektów Article na tekst
    body = "\n".join(str(article) for article in articles)
    msg.attach(MIMEText(body, 'plain'))

    # Zakoduj wiadomość jako base64
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    # Wyślij wiadomość
    message = {'raw': raw}
    service.users().messages().send(userId='me', body=message).execute()
