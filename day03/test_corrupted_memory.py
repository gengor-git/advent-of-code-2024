import unittest
import day03.corrupted_memory as this_day

class TestCorruptedMemory(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.mult_corrputed_memory(this_day.sample_file), 161)

    def testInputPart1(self):
        self.assertEqual(this_day.mult_corrputed_memory(this_day.input_file), 173785482)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.mult_corrputed_instr_memory(this_day.sample_file_instr), 48)

    def testInputPart2(self):
        self.assertEqual(this_day.mult_corrputed_instr_memory(this_day.input_file), 83158140)
        
