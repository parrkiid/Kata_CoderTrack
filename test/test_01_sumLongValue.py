import unittest
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from sumLongValue import sumLongValue
from sumLongValue import CARRY_NUMBER_when_Sum_MoreThan_9
from sumLongValue import OUTPUT_when_Sum_MoreThan_9

class testsumLongValue(unittest.TestCase):

    def test_input2Numbers_Should_Be_Return_Sum_of_theirs(self):
        INPUT1 = "341958380513922689345579269516458072674896"
        INPUT2 = "452266679609279263090069747948272865233879"
        EXPECTED_RESULT = "794225060123201952435649017464730937908775"
        RETURN_RESULT = sumLongValue(INPUT1,INPUT2)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)
    
    def test_CARRY_NUMBER_when_Sum_MoreThan_9_ShouldBe_Return_FirstPosition(self):
        INPUT = "12"
        EXPECTED_RESULT = "1"
        RETURN_RESULT = CARRY_NUMBER_when_Sum_MoreThan_9(INPUT)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_CARRY_NUMBER_when_Sum_LessThan_10_ShouldBe_Return_0(self):
        INPUT = "9"
        EXPECTED_RESULT = "0"
        RETURN_RESULT = CARRY_NUMBER_when_Sum_MoreThan_9(INPUT)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_OUTPUT_when_Sum_MoreThan_9_ShouldBe_Return_LastNumber(self):
        INPUT = "12"
        EXPECTED_RESULT = "2"
        RETURN_RESULT = OUTPUT_when_Sum_MoreThan_9(INPUT)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_OUTPUT_when_Sum_LessThan_10_ShouldBe_Return_InputNumber(self):
        INPUT = "9"
        EXPECTED_RESULT = "9"
        RETURN_RESULT = OUTPUT_when_Sum_MoreThan_9(INPUT)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testsumLongValue)
    unittest.TextTestRunner(verbosity=2).run(suite)

