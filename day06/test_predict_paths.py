import unittest
import day06.predict_paths as this_day

class TestSomethingSomething(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_predicted_visits(this_day.sample_file), 41)

    def testInputPart1(self):
        self.assertEqual(this_day.count_predicted_visits(this_day.input_file), 5067)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.count_loop_by_obstacle(this_day.sample_file), 6)

    def testInputPart2(self):
        self.assertEqual(this_day.count_loop_by_obstacle(this_day.input_file), 1793)
        
