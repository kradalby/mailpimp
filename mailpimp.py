#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import email
import sys
import os
import logging
import configparser

from list import ListManager
from mailgun import MailGunSMTP

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('MailPimp')

CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + "/" + "config.ini"


class MailPimp():
    def __init__(self, sender, recipient, mail):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)

        self.mg = MailGunSMTP(
            self.config["mailgun"]["user"],
            self.config["mailgun"]["password"]
        )
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
            self.mg.send_message(
                self.mail["From"],
                list.get_recipients(),
                self.mail
            )

        else:
            logger.info("Sender %s, is not authorized to send to %s" %
                        (self.sender, self.recipient))

    def get_attachments(self):
        files = []
        if self.mail.is_multipart():
            for file in self.mail.get_payload():
                files.append((file.get_filename(), file.get_payload()))
            return files
        return files


if __name__ == '__main__':
    try:
        mail = email.message_from_binary_file(sys.stdin.buffer)
        sender = sys.argv[1]
        recipient = sys.argv[2]

        logger.debug("######################")
        logger.debug("To: %s" % recipient)
        logger.debug("From: %s" % sender)
        logger.debug("Subject: %s" % mail["Subject"])
        logger.debug("######################\n")

        mp = MailPimp(sender, recipient, mail)
        mp.distribute()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
