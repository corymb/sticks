import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LogHandler(object):
    def __init__(self, location=None):
        self.location = location if location else os.environ.get(
            'ZNC_LOG_LOCATION', '.')
        logger.info('LogHandler location set to {}'.format(self.location))

    def get_logs_list(self):
        return sorted(
            [f for f in os.listdir(self.location) if f.endswith('.log')])
