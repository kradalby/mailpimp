#!/usr/bin/env python3

import email
import sys
import logging

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('mailpimp')

try:
    logger.info("trying to read mail")
    sender = sys.argv[0]
    recipient = sys.argv[1]
    msg = email.message_from_binary_file(sys.stdin.buffer)
    
    logger.info(sender, recipient)
    logger.info(msg)
    logger.info(dir(msg))
except Exception as e:
    logger.exception(e)
    sys.exit(1)
