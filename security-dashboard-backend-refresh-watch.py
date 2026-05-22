from dotenv import load_dotenv
load_dotenv()

from gmail_gcloud import gmail_service
import os

result = gmail_service.users().watch(
    userId=os.getenv('GMAIL_USER_ID'),
    body={
        'topicName': 'projects/heroic-gamma-434513-h9/topics/gmail-notifications',
        'labelIds': ['INBOX'],        # omit to watch everything
        'labelFilterAction': 'include',
    }
).execute()

print(result)
