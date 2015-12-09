# Mailpimp
[![Build Status](https://drone.fap.no/api/badges/kradalby/mailpimp/status.svg)](https://drone.fap.no/kradalby/mailpimp)

Mailpimp is a poormans info mailinglist manager written in Python 3. It uses Postfix to get the mails, and Mailgun to send mails. Mailgun can easily be changed with your own SMTP server

## Postfix setup

### main.cf
local_recipient_maps =
local_transport = mailpimp
mailpimp_destination_recipient_limit = 1

mydestination = butterfree.fap.no, localhost.fap.no, localhost, lists.somedomain.no

### master.cf
mailpimp    unix    -       n       n       -       -       pipe
  user=someuser argv=/srv/mailpimp/env/bin/python /srv/mailpimp/mailpimp.py ${sender} ${recipient}
