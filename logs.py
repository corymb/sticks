import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
                    message_list.append(line.strip())
        return message_list
