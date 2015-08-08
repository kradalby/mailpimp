import os
import unittest

TEST_LISTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lists_test.mp')


class MailPimpTests(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(1, 1)
