import unittest

from task import *


def isEqual(x, y, precision=0.0000000000000000001):
    return abs((x - y) / x) < precision

class TestCase(unittest.TestCase):
    def test_FixPoint(self):
        self.assertTrue(isEqual(fixPoint(lambda x: 1 + x / 2), 2))

    def test_Sqrt9(self):
        self.assertTrue(isEqual(sqrt(9), 3))
