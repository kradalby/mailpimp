import requests
import logging

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('MailGun')

class MailGun():
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def send_message(self, fr, to, subject, content):
        return requests.post(
            self.url,
            auth=("api", self.key),
            data={
                "from": fr,
                "to": to,
                "subject": subject,
                "text": content
            })
