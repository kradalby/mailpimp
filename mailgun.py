import requests
import logging
import smtplib

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('MailGun')

class MailGunHTTP():
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def send_message(self, fr, to, subject, content, files):
        f = [("attachment", x) for x in files]
        return requests.post(
            self.url,
            auth=("api", self.key),
            files=f,
            data={
                "from": fr,
                "to": to,
                "subject": subject,
                "text": content
            })

class MailGunSMTP():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def send_message(self, fr, to, mail):
        s = smtplib.SMTP('smtp.mailgun.org', 587)
        logger.debug("SMTP login: %s %s" % (self.user, self.password))
        s.login(self.user, self.password)

        s.sendmail(fr, to, mail.as_string())
        s.quit()


