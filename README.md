## idea_sms_sdk

idea_sms_sdk is a Python library for sending sms from idea sms platform

## Installation

Use the package manager pip to install idea_sms_sdk.

```bash
pip install idea_sms_sdk
```

## Usage

```python
from idea_sms_sdk.messaging import SMS

Initialize the sdk
api = SMS(sender_id='your_sender_id', api_key='your_api_key', partner_id='yourpartner_id')

# send sms message

sms = api.send_sms(phone_numbers=['07123456789'], message_text='Hello from Idea Sms') #returns a json object.

delivery_report = api.delivery_report(message_id='your_message_id') #returns a json object

account_balance = api.account_balance() #returns a json object

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
