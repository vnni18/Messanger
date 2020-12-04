import requests

name = input('Your Name: ')

while True:
    text = input('Your Messange: ')
    requests.post(
        'http://127.0.0.1:5000/send',
        json = {
            'name': name,
            'text': text
        }
    )