import os


class LogHandler(object):
    def __init__(self, location=None):
        self.location = location if location else os.environ.get(
            'ZNC_LOG_LOCATION', '.')

    def get_logs_list(self):
        return sorted(
            [f for f in os.listdir(self.location) if f.endswith('.log')])
