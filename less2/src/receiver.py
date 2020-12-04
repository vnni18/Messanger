from datetime import datetime

import requests
import time

def print_messange(messange):
    new_time = datetime.fromtimestamp(messange['time'])
    new_time = new_time.strftime('%Y/%m/%d %H:%M')
    print(new_time, messange['name'])
    print(messange['text'])
    print()

after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messanges',
        params = {
            'after': after
        }
    )
    response_data = response.json()

    for messange in response_data['messanges']:
        print_messange(messange)
        after = messange['time']

    time.sleep(1)