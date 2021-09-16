import unittest

from task import sumInts


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_sumInts(self):
        self.assertEqual(sumInts(5, 10), 45)
