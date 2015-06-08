#!/usr/bin/env python3

import email
import sys
import logging

logger = logging.getLogger('mailpimp')

msg = email.message_from_binary_file(sys.stdin.buffer)

logger.info(msg)
logger.info(dir(msg))
