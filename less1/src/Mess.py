
messange1 = {
    'name': 'Mary',
    'text': 'Mess1',
    'time': 'time1'
}
messange2 = {
    'name': 'Nike',
    'text': 'Mess2',
    'time': 'time2'
}

db = [
    messange1,
    messange2
]

def send_messange(name, text):
    new_message = {
        'name': name,
        'text': text,
        'time': 'time3'
    }
    db.append(new_message)

def get_messange():
    return db

def print_messanges(messanges):
    for messange in messanges:
        print(messange['time'], messange['name'])
        print(messange['text'])