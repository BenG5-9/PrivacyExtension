import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# only need the mail scope
SCOPES = ["https://mail.google.com/"]


def connect_api():
  creds = None
  # token.json used to keep authentication. Create if one is not there
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES #read from the ceated credentials
      )
      creds = flow.run_local_server(port=0)
    # save the credentials
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    return creds

  except HttpError as error:
    print(f"An error occurred: {error}")
    return 0

def send_opt_out(to, message):
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id
"""

  try:
    creds = connect_api()
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    message.set_content(message)

    message["To"] = to
    message["Subject"] = "Opt-out"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message