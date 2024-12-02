import unittest
import day02.analyze_reports as this_day

class TestCountSafeReports(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_safe_reports(this_day.sample_file), 2)

    def testInputPart1(self):
        self.assertEqual(this_day.count_safe_reports(this_day.input_file), 326)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.count_safe_reports_with_dampener(this_day.sample_file), 4)

    def testInputPart2(self):
        self.assertEqual(this_day.count_safe_reports_with_dampener(this_day.input_file), 381)
        
