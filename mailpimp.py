#!/usr/bin/env python3

import configparser
import email
import logging
import os
import sys

from list import ListManager

CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + '/' + 'config.ini'
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
        else:
            logger.info('Sender %s, is not authorized to send to %s' %
                        (self.sender, self.recipient))


if __name__ == '__main__':
    try:
        mail = email.message_from_binary_file(sys.stdin.buffer)
        sender = sys.argv[1]
        recipient = sys.argv[2]

        logger.debug('To: %s, From: %s' % (recipient, sender))

        mp = MailPimp(sender, recipient, mail)
        mp.distribute()
    except Exception as e:
        logger.exception(e)
        sys.exit(1)
