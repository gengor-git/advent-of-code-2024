import unittest
import day05.print_updates as this_day

class TestPrintUpdates(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.sum_mid_page_updates(this_day.sample_file), 143)

    def testInputPart1(self):
        self.assertEqual(this_day.sum_mid_page_updates(this_day.input_file), 7198)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.fix_and_sum_mid_page_updates(this_day.sample_file), 123)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
