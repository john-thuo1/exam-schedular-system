import requests


def send(phone_number, message="Hi from Africa's Talking"):
    payload = {
        "username": 'sandbox',
        "to": f"+{phone_number}",
        "message": message,
        "from": 23051 # short code
    }

    header = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        # enter your api key here
        'apiKey': '7141b829cf6ae244cda1b3c7f7b5f0168912264ff6438f2d5dee3e335d15da03'
    }

    req = requests.post('https://api.sandbox.africastalking.com/version1/messaging', data=payload, headers=header)

    req = req.json()
    message_data = req['SMSMessageData']
    status = message_data["Recipients"][0]['status']

    return status
