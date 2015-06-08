from list import ListManager
#from mailpimp import allowed

import os

TEST_LISTS = os.path.dirname(os.path.abspath(__file__)) + "/" + "lists_test.mp"

def test_test():
    assert(1 == 1)

#def test_allowed():
#    lm = ListManager(TEST_LISTS)
#
#    assert(allowed(lm, "derp@example.com", "sender@example.com"))
#    assert(allowed(lm, "derp1@example.com", "sender3@example.com"))
#    assert(not allowed(lm, "derp2@example.com", "sender5@example.com"))
#    assert(not allowed(lm, "derp3@example.com", "senderi6@example.com"))
#
