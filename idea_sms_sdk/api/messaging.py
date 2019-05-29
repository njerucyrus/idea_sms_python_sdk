import hashlib
import json
import uuid
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import fromstring

import requests

from idea_sms_sdk.api import CleanPhoneNumber


class SMS(object):
    def __init__(self, user_id=None, password=None, sender_id=None, account_url='http://sms.ideasms.co.ke/'):
        self._user_id = user_id
        self._password = password
        self._base_url = account_url
        self._sender_id = None

        if self._user_id is None or user_id.strip() == '':
            raise ValueError("user id cannot be empty")
        if type(self._user_id) is not str:
            raise TypeError("user_id must be a string")

        if self._password is None or self._password.strip() == '':
            raise ValueError('password cannot be empty')

        if type(self._password) is not str:
            raise TypeError('password must be a string')

    def send_sms(self, phone_numbers=None, message_text=None):

        """
        :param phone_numbers: list of recipients phone numbers eg phone_numbers=['994340340934, '39303409340']
        :param message_text: a text messages you want to send
        :returns json object:

        if message was sent successfully:
             ********
            -smsclientid : str
            -messageid: str

        if there was an error while sending
            ********
            -smsclientid: str
            -error_code: str
            -error_description: str
            -error_action: str
        """

        xml_root = etree.Element('smslist')

        if type(phone_numbers) is not list:
            raise TypeError("phone_numbers must be a list")
        if len(phone_numbers) == 0:
            raise ValueError('phone_numbers cannot be an empty list')
        if message_text is None or message_text.strip() == '':
            raise ValueError('message_text cannot be empty string')

        for phone_number in phone_numbers:
            sms = etree.SubElement(xml_root, 'sms')

            user = etree.SubElement(sms, 'user')
            user.text = self._user_id

            password = etree.SubElement(sms, 'password')
            password.text = self._password

            mobiles = etree.SubElement(sms, 'mobiles')
            mobiles.text = CleanPhoneNumber(phone_number).sanitize_phone_number()

            message = etree.SubElement(sms, 'message')
            message.text = message_text

            if self._sender_id:
                sender_id = etree.SubElement(sms, 'senderid')
                sender_id.text = self._sender_id

            client_sms_id = etree.SubElement(sms, 'clientsmsid')
            client_sms_id.text = hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()

            unicode = etree.SubElement(sms, 'unicode')
            unicode.text = 0

        url = "{0}{1}".format(self._base_url, "/sendsms.jsp")

        headers = {'Content-Type': 'application/xml'}

        xmlstr = etree.tostring(xml_root, encoding='iso-8859-1', method='xml')

        req = requests.post(url=url, data=xmlstr, headers=headers)

        api_response = {}

        if req.status_code == 200:
            xml_res = fromstring(req.text)

            for item in xml_res.getchildren():

                for res_item in item.getchildren():
                    api_response[res_item.tag.replace('-', '_')] = res_item.text

        return json.dumps(api_response)
