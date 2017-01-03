import os
from test.test_support import EnvironmentVarGuard

from twisted.trial import unittest

from logs import LogHandler

TEST_LOG_FILE_METADATA = {
    'total_length': 76,
    'first_head': '[00:48:30] <asdf> _habnabit yes heartache is amazing',
    'second_head': '[04:10:55] <toddpratt> but the only way to diagnose '
    'it positively is via autopsy',
    'third_head': '[05:36:39] <Jerub> is the daydream vr thing any good?'
}


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
        self.assertItemsEqual(self.log_handler.get_logs_list(), sorted(
            self.log_files))

    def test_get_message_list(self):
        message_list = self.log_handler.get_message_list()
        self.assertEqual(
            len(message_list), TEST_LOG_FILE_METADATA['total_length'])

    def test_message_does_not_end_with_new_line(self):
        message_list = self.log_handler.get_message_list()
        for m in message_list:
            self.assertFalse(m.endswith('\\n'))

    def test_get_message_list_order(self):
        message_list = self.log_handler.get_message_list()
        self.assertEqual(
            message_list[0], TEST_LOG_FILE_METADATA['first_head'])
        self.assertEqual(
            message_list[25], TEST_LOG_FILE_METADATA['second_head'])
        self.assertEqual(
            message_list[51], TEST_LOG_FILE_METADATA['third_head'])
