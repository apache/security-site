from google.auth.transport.requests import Request
from google.cloud import pubsub_v1
from google.oauth2.credentials import Credentials
import os

SCOPES = ['https://www.googleapis.com/auth/pubsub']

creds = Credentials(
          token=None,
          refresh_token=os.getenv('PUBSUB_OAUTH_REFRESH_TOKEN'),
          token_uri="https://oauth2.googleapis.com/token",
          client_id=os.getenv('PUBSUB_OAUTH_CLIENT_ID'),
          client_secret=os.getenv('PUBSUB_OAUTH_CLIENT_SECRET'),
          scopes=SCOPES,
)
creds.refresh(Request())

gmail_subscriber = pubsub_v1.SubscriberClient(credentials=creds)
subscription_path = gmail_subscriber.subscription_path(
    "security-gmail-pubsub",
    "listen-for-email-updates"
)

def gmail_subscribe(callback):
    return gmail_subscriber.subscribe(subscription_path, callback=callback)
