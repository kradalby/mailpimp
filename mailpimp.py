#!/usr/bin/env python3

import email
import sys
import logging
import configparser

from list import ListManager

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('mailpimp')


class MailPimp():
    def __init__(self, sender, recipient, mail):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.lm = ListManager(self.config["list"]["list_file"])

        self.sender = sender
        self.recipient = recipient
        self.mail = mail

    def allowed(self, recipient, sender):
        list = self.lm.get_list(recipient)
        if list and sender in list.get_senders():
            return True
        return False

    def distribute(self):
        if self.allowed(self.recipient, self.sender):
            logger.info("Sender %s, is authorized to send to %s" %
                        (self.sender, self.recipient))

if __name__ == '__main__':
    try:
        mail = email.message_from_binary_file(sys.stdin.buffer)
        sender = sys.argv[0]
        recipient = sys.argv[1]

        mp = MailPimp(sender, recipient, mail)
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
