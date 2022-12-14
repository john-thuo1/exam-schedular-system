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
        #e.g 'apiKey': 'e1afe82a388175d7f4230297acb58dd039ba0135541ae1987a4d9d88455d07da3'

        'apiKey': '********************************************************************'
    }

    req = requests.post('https://api.sandbox.africastalking.com/version1/messaging', data=payload, headers=header)

    req = req.json()
    message_data = req['SMSMessageData']
    status = message_data["Recipients"][0]['status']

    return status
