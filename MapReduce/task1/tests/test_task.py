import unittest

from task import *


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_sumInts(self):
        self.assertEqual(sumInts(5, 10), 45)

    def test_performance_sumInts(self):
        self.assertEqual(sumInts(5, 100000), 705082694)

    def test_sumCube(self):
        self.assertEqual(sumCube(5, 10), 2925)

    def test_sumFact(self):
        self.assertEqual(sumFact(5, 10), 4037880)
