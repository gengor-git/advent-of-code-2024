import unittest
import day06.predict_paths as this_day

class TestSomethingSomething(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_predicted_steps(this_day.sample_file), 41)

    def testInputPart1(self):
        self.assertEqual(this_day.count_predicted_steps(this_day.input_file), 3246517)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
