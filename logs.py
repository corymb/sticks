import os
import re
import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Line = namedtuple('Line', ('time', 'nick', 'message'))

class LogHandler(object):
    def __init__(self, location=None):
        self.location = location if location else os.environ.get(
            'ZNC_LOG_LOCATION', '.')
        # logger.info('LogHandler location set to {}'.format(self.location))

    def get_logs_list(self):
        return sorted(
            [f for f in os.listdir(self.location) if f.endswith('.log')])

    def get_message_list(self):
        message_list = []
        for f in self.get_logs_list():
            with open(self.location + '/' + f) as log_file:
                for line in log_file:
                    if not '***' in line:  # Crapbuster.
                        message_list.append(
                            self.get_message_data(line))
        return message_list

    def extract_time(self, line):
        return re.search(r'\[.*?\]', line).group(0)

    def extract_nick(self, line):
        return re.search(r'\<.*?\>', line).group(0)

    def extract_message(self, line):
        return re.search(r'>(.*)$', line).group(1).strip()

    def get_message_data(self, line):
        time = self.extract_time(line)
        nick = self.extract_nick(line)
        message = self.extract_message(line)
        return Line(time, nick, message)
