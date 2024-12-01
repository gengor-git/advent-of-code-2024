import unittest
import day01.calculate_distances as day1

class TestCalculateDistances(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(day1.calculate_distances(day1.sample_file), 11)

    def testInputPart1(self):
        self.assertEqual(day1.calculate_distances(day1.input_file), 3246517)
        