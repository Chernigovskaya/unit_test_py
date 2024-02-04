from unittest import TestCase
from number_in_interval import number_in_interval


class Test(TestCase):
    def test_number_in_interval_yes(self):
        self.assertTrue(number_in_interval(30))

    def test_number_in_interval_less(self):
        self.assertFalse(number_in_interval(20))

    def test_number_in_interval_more(self):
        self.assertFalse(number_in_interval(100))
