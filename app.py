from flask import Flask, request
from sender import Sender
import os
import datetime

url = os.environ.get("HEC_URL")
token = os.environ.get("HEC_TOKEN")
format = os.environ.get("HEC_FORMAT")
time_format = os.environ.get("HEC_TIME_FORMAT")

if url is None:
    print("HEC_URL must be set")
    exit(1)
if token is None:
    print("HEC_TOKEN must be set")
    exit(1)
if time_format is None:
    time_format = "%Y-%m-%d %H:%M:%S"

sender = Sender(url, token)

app = Flask(__name__)

@app.route("/event/<subtype>", methods=["PUT", "POST"])
def hello_world(subtype):
    event = request.get_json()
    for key in event:
        if (str(key)).endswith("Date"):
            event[key] = datetime.datetime.fromtimestamp(int(event[key]) / 1000).strftime(time_format)
    if format is None:
        msg = ""
        first = True
        for key in event:
            if not first:
                msg += ", "
            first = False
            msg += key
            msg += ": "
            msg += str(event[key])
        sender.send_message(msg)
    else:
        sender.send_message(format.format_map(event))
    return 'OK'