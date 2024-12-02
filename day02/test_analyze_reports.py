import unittest
import day02.analyze_reports as this_day

class TestCalculateSomething(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_safe_reports(this_day.sample_file), 2)

    def testInputPart1(self):
        self.assertEqual(this_day.count_safe_reports(this_day.input_file), 3246517)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
