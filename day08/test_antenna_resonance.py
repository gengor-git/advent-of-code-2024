import unittest
import day08.antenna_resonance as this_day

class TestAntennaResonance(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.count_resonance_spots(this_day.sample_file), 14)

    def testInputPart1(self):
        self.assertEqual(this_day.count_resonance_spots(this_day.input_file), 269)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.count_resonance_spots2(this_day.sample_file), 34)

    def testInputPart2(self):
        self.assertEqual(this_day.count_resonance_spots2(this_day.input_file), 949)
        
