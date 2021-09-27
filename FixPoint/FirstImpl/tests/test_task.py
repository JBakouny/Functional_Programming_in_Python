import unittest

from task import fixPoint


def isEqual(x, y, precision=0.0000000000000000001):
    return abs((x - y) / x) < precision

class TestCase(unittest.TestCase):
    def test_FixPoint(self):
        self.assertTrue(isEqual(fixPoint(lambda x: 1 + x / 2), 2))
