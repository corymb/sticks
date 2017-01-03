import os
from test.test_support import EnvironmentVarGuard

from twisted.trial import unittest

from logs import LogHandler


class LogHandlingTests(unittest.TestCase):
    def setUp(self):
        self.log_handler = LogHandler(os.path.dirname(__file__))
        self.log_files = ['2016-12-28.log', '2016-12-29.log', '2016-12-30.log']

    def test_log_location_constructor(self):
        log_handler = LogHandler('TEST')
        self.assertEqual(log_handler.location, 'TEST')

    def test_log_location_env_var(self):
        env = EnvironmentVarGuard()
        env.set('ZNC_LOG_LOCATION', 'TEST')
        log_handler = LogHandler()
        with env:
            self.assertEqual(log_handler.location, 'TEST')

    def test_log_location_fallback(self):
        log_handler = LogHandler()
        self.assertEqual(log_handler.location, '.')

    def test_files_listed(self):
        self.assertItemsEqual(self.log_handler.get_logs_list(), self.log_files)

    def test_only_log_files_listed(self):
        for f in self.log_handler.get_logs_list():
            self.assertTrue(f.endswith('log'))

    def test_log_file_order(self):
        self.assertItemsEqual(self.log_handler.get_logs_list(), sorted(self.log_files))



