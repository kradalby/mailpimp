import logging

logging.basicConfig(filename="/var/log/mailpimp.log", level=logging.DEBUG)
logger = logging.getLogger('MailPimpList')

class ListManager():
    def __init__(self, list_file):
        self.lists = {}
        with open(list_file, 'r') as file:
            lists = [x for x in file.read().split('\n') if x]
            for list_string in lists:
                list = List(list_string)
                self.lists[list.name] = list
                logger.debug("Added list %s" % list.get_name())

    def get_list(self, name):
        if name in self.lists.keys():
            return self.lists[name]
        return None

    def get_lists(self):
        return self.lists


class List():
    def __init__(self, list_string):
        self.name = list_string.split(":")[0]
        self.senders = list_string.split(":")[1].split(" ")
        self.resipients = list_string.split(":")[2].split(" ")

    def get_name(self):
        return self.name

    def get_senders(self):
        return self.senders

    def get_recipients(self):
        return self.resipients
