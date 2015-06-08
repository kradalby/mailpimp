from list import List, ListManager
import os

TEST_LISTS = os.path.dirname(os.path.abspath(__file__)) + "/" + "lists_test.mp"

def test_list_manager_creation():
    lm = ListManager(TEST_LISTS)
    assert(len(lm.lists) == 4)

    l1 = lm.get_list("erp@example.com")
    l2 = lm.get_list("derp@example.com")

    assert(l1 == None)
    assert(l2 != None)

def test_list_name():
    lm = ListManager(TEST_LISTS)

    l = lm.get_list("derp@example.com")
    assert(l.get_name() == "derp@example.com")

def test_list_senders():
    lm = ListManager(TEST_LISTS)

    l1 = lm.get_list("derp@example.com")
    l2 = lm.get_list("derp1@example.com")
    l3 = lm.get_list("derp2@example.com")
    l4 = lm.get_list("derp3@example.com")

    assert(len(l1.get_senders()) == 1)
    assert(len(l2.get_senders()) == 4)
    assert(len(l3.get_senders()) == 1)
    assert(len(l4.get_senders()) == 4)

def test_list_recipients():
    lm = ListManager(TEST_LISTS)

    l1 = lm.get_list("derp@example.com")
    l2 = lm.get_list("derp1@example.com")
    l3 = lm.get_list("derp2@example.com")
    l4 = lm.get_list("derp3@example.com")

    assert(len(l1.get_recipients()) == 1)
    assert(len(l2.get_recipients()) == 1)
    assert(len(l3.get_recipients()) == 4)
    assert(len(l4.get_recipients()) == 4)
