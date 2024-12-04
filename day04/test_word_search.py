import unittest
import day04.word_search as this_day

class TestWordSearch(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_xmas(this_day.sample_file), 18)

    def testInputPart1(self):
        self.assertEqual(this_day.count_xmas(this_day.input_file), 2551)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
