import time
import datetime

messange1 = {
    'name': 'Mary',
    'text': 'Mess1',
    'time': time.time()
}
messange2 = {
    'name': 'Nike',
    'text': 'Mess2',
    'time': time.time()
}

db = [
    messange1,
    messange2
]

def send_messange(name, text):
    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)

def get_messange(after = 0):
    messanges = []
    for messange in db:
        if messange['time'] > after:
            messanges.append(messange)
    return messanges

def print_messanges(messanges):
    for messange in messanges:
        new_time = datetime.datetime.fromtimestamp(messange['time'])
        new_time = new_time.strftime('%Y/%m/%d %H:%M')
        print(new_time, messange['name'])
        print(messange['text'])