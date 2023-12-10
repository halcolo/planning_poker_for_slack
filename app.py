import logging

logging.basicConfig(level=logging.INFO)

import json
import os
from config import BOT_ID, signature_verifier
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import make_response


with open(os.path.join("templates", "poker_modal.json")) as file:
    poker_modal_data = json.load(file)
    
    
app = App()
    
@app.command("/new-poker")
def handle_poker_view(body, ack, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=poker_modal_data,
    )
    
@app.view("poker-modal")
def handle_view_submission_poker_events(ack, body):
    ack()
    print('-'*50)
    print(body["view"]["state"]["values"])
    print('-'*50)
    # logger.info(body)

from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

