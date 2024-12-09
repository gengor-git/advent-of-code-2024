import unittest
import day09.disk_fragmenter as this_day

class TestSomethingSomething(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.defrag_part1(this_day.sample_file), 11)

    def testInputPart1(self):
        self.assertEqual(this_day.defrag_part1(this_day.input_file), 3246517)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
