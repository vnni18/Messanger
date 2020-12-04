
import time
from datetime import datetime
from flask import Flask, request, abort

app = Flask(__name__)

db = [
    {
        'name': 'Mary',
        'text': 'Mess1',
        'time': time.time()
    }, {
        'name': 'Nike',
        'text': 'Mess2',
        'time': time.time() +1
    }
]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    dt = datetime.now()
    return {
        'status': True,
        'name': 'NameServer',
        'time': dt.strftime('%Y/%m/%d %H:%M')
    }

@app.route("/send", methods = ['POST'])
def send_messange():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(request.json.get('name'), str) or not isinstance(request.json.get('text'), str):
        return abort(400)
    if not name or not text:
        return abort(400)

    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)
    return {
        'OK': True
    }

@app.route("/messanges")
def get_messange():
    try:
        after = float(request.args.get('after', 0))
    except ValueError:
        return abort(400)

    messanges = []
    for messange in db:
        if messange['time'] > after:
            messanges.append(messange)
    return {
        'messanges': messanges
    }

app.run()