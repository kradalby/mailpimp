import os
import unittest

from list import ListManager

TEST_LISTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lists_test.mp')


class ListManagerTests(unittest.TestCase):
    def test_list_manager_creation(self):
        lm = ListManager(TEST_LISTS)
        self.assertEqual(len(lm.lists), 4)

        l1 = lm.get_list('erp@example.com')
        l2 = lm.get_list('derp@example.com')

        self.assertEqual(l1, None)
        self.assertNotEqual(l2, None)

    def test_list_name(self):
        lm = ListManager(TEST_LISTS)

        l = lm.get_list('derp@example.com')
        self.assertEqual(l.get_name(), 'derp@example.com')

    def test_list_senders(self):
        lm = ListManager(TEST_LISTS)

        l1 = lm.get_list('derp@example.com')
        l2 = lm.get_list('derp1@example.com')
        l3 = lm.get_list('derp2@example.com')
        l4 = lm.get_list('derp3@example.com')

        self.assertEqual(len(l1.get_senders()), 1)
        self.assertEqual(len(l2.get_senders()), 4)
        self.assertEqual(len(l3.get_senders()), 1)
        self.assertEqual(len(l4.get_senders()), 4)

    def test_list_recipients(self):
        lm = ListManager(TEST_LISTS)

        l1 = lm.get_list('derp@example.com')
        l2 = lm.get_list('derp1@example.com')
        l3 = lm.get_list('derp2@example.com')
        l4 = lm.get_list('derp3@example.com')

        self.assertEqual(len(l1.get_recipients()), 1)
        self.assertEqual(len(l2.get_recipients()), 1)
        self.assertEqual(len(l3.get_recipients()), 4)
        self.assertEqual(len(l4.get_recipients()), 4)
