import unittest

from task import *


def equals(x, y):
    return abs((y - x) / x) < 0.001


class TestCase(unittest.TestCase):
    def test_sqrtFloatImprecision(self):
        self.assertEqual(sqrt(9), 3, msg="Floating-point imprecision")

    def test_sqrtCorrect(self):
        self.assertTrue(equals(sqrt(9), 3))
