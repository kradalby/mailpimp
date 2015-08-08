#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import email
import logging
import os
import sys

from list import ListManager
from mailgun import MailGunSMTP

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join('mailpimp.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '*': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

logger = logging.getLogger(__name__)


class MailPimp():
    def __init__(self, sender, recipient, mail):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)
        self.lm = ListManager(self.config['list']['list_file'])
        self.mg = MailGunSMTP(
            self.config["mailgun"]["user"],
            self.config["mailgun"]["password"]
        )

        logging.basicConfig(filename=self.config['log']['file'], level=logging.DEBUG)
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
            logger.info('Sender %s, is authorized to send to %s' %
                        (self.sender, self.recipient))
            list = self.lm.get_list(self.recipient)
            self.mg.send_message(
                self.mail["From"],
                list.get_recipients(),
                self.mail
            )

        else:
            logger.info('Sender %s, is not authorized to send to %s' %
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

<<<<<<< HEAD
        logger.debug('To: %s, From: %s' % (recipient, sender))
=======
        logger.debug("######################")
        logger.debug("To: %s" % recipient)
        logger.debug("From: %s" % sender)
        logger.debug("Subject: %s" % mail["Subject"])
        logger.debug("######################\n")
>>>>>>> faff4c626946a2d91bd6e395869f530024c6f826

        mp = MailPimp(sender, recipient, mail)
        mp.distribute()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
