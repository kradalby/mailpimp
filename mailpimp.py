#!/usr/bin/env python3

import email
import sys
import os
import logging
import configparser

from list import ListManager
from mailgun import MailGun

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('MailPimp')

CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + "/" + "config.ini"


class MailPimp():
    def __init__(self, sender, recipient, mail):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)

        self.mg = MailGun(self.config["mailgun"]["url"], self.config["mailgun"]["key"])
        self.lm = ListManager(self.config["list"]["list_file"])

        logger.debug(self.lm.get_lists())

        self.sender = sender
        self.recipient = recipient
        self.mail = mail

    def allowed(self):
        list = self.lm.get_list(self.recipient)
        if list and self.sender in list.get_senders():
            return True
        return False

    def distribute(self):
        if self.allowed():
            logger.info("Sender %s, is authorized to send to %s" %
                        (self.sender, self.recipient))
            list = self.lm.get_list(self.recipient)
            response =self.mg.send_message(
                self.mail["From"], 
                list.get_recipients(), 
                self.mail["Subject"], 
                self.mail.get_payload()
            )
            logger.debug(response)
        else:
            logger.info("Sender %s, is not authorized to send to %s" %
                        (self.sender, self.recipient))


if __name__ == '__main__':
    try:
        mail = email.message_from_binary_file(sys.stdin.buffer)
        logger.debug(dir(mail))
        logger.debug(mail["From"])
        logger.debug(mail.get_payload())
        sender = sys.argv[1]
        recipient = sys.argv[2]

        logger.debug("To: %s, From: %s" % (recipient, sender))

        mp = MailPimp(sender, recipient, mail)
        mp.distribute()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
