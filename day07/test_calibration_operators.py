import unittest
import day07.calibration_operators as this_day

class TestCalibrationOperators(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.sum_total_calibration_results(this_day.sample_file), 3749)

    def testInputPart1(self):
        self.assertEqual(this_day.sum_total_calibration_results(this_day.input_file), 538191549061)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.sum_total_calibration_results2(this_day.sample_file), 11387)

    def testInputPart2(self):
        self.assertEqual(this_day.sum_total_calibration_results2(this_day.input_file), 34612812972206)
        
