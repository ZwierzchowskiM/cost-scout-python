import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

def authenticate_gmail():

    try:
        load_dotenv()

        client_id = os.getenv("GOOGLE_OAUTH2_CLIENT_ID")
        client_secret = os.getenv("GOOGLE_OAUTH2_CLIENT_SECRET")
        refresh_token = os.getenv("GOOGLE_OAUTH2_REFRESH_TOKEN")

        if not client_id or not client_secret or not refresh_token:
            raise ValueError("Brak wymaganych danych do uwierzytelnienia Gmail API.")

        creds = Credentials.from_authorized_user_info(
            info={
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token,
                'token': '', 
            },
        )

        if creds.expired or not creds.valid:
            creds.refresh(Request())

        return creds
    
    except Exception as e:
        print(f"Błąd uwierzytelnienia Gmail API: {e}")
        return None  # Można obsłużyć błąd w `send_email`
    
    
def send_email(subject, articles, to_email):
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    msg = MIMEMultipart()
    msg['From'] = 'me'
    msg['To'] = to_email
    msg['Subject'] = subject

    body = "\n".join(str(article) for article in articles)
    msg.attach(MIMEText(body, 'plain'))

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    message = {'raw': raw}
    service.users().messages().send(userId='me', body=message).execute()
