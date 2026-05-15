from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = Credentials(
          token=None,
          refresh_token=os.getenv('GMAIL_OAUTH_REFRESH_TOKEN'),
          token_uri="https://oauth2.googleapis.com/token",
          client_id=os.getenv('GMAIL_OAUTH_CLIENT_ID'),
          client_secret=os.getenv('GMAIL_OAUTH_CLIENT_SECRET'),
          scopes=['https://www.googleapis.com/auth/gmail.readonly'],
)
creds.refresh(Request())

# careful: service objects should not be shared across threads
gmail_service = build('gmail', 'v1', credentials=creds)

def history_from(start_history_id):
    request = gmail_service.users().history().list(
        userId=os.getenv('GMAIL_USER_ID'),
        startHistoryId=start_history_id,
        # this hits
        # https://github.com/googleapis/google-api-python-client/issues/667
        # https://github.com/googleapis/google-api-python-client/issues/2178
        #historyTypes=['labelAdded', 'labelRemoved', 'messageAdded', 'messageDeleted'],
        # for now just catching all changes might be fine.
    )

    records = []
    while request is not None:
        response = request.execute()
        records.extend(response.get('history', []))
        request = gmail_service.users().history().list_next(request, response)

    return records

def messages_by_label(label_id):
    request = gmail_service.users().messages().list(
            userId=os.getenv('GMAIL_USER_ID'),
            labelIds=[ label_id ]
    )

    messages = []
    while request is not None:
        response = request.execute()
        messages.extend(response.get('messages', []))
        request = gmail_service.users().messages().list_next(request, response)

    return messages
