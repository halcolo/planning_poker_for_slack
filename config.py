import slack
import os
from slack_bolt import App
from slack_sdk.signature import SignatureVerifier
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import logging
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler


logging.basicConfig(level=logging.ERROR)

# Load the tokens from .env file
dot_env_path = Path('.') / '.env'
load_dotenv(dotenv_path=dot_env_path)

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
BOT_ID = client.api_call("auth.test")["user_id"]
signature_verifier = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])


app = App()
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# app = App(
#     token=os.environ['SLACK_BOT_TOKEN'],
#     signing_secret=os.environ["SLACK_SIGNING_SECRET"],
# )

