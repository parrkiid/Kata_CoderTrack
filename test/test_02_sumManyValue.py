import unittest
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from sumManyValue import sumManyValue
from sumManyValue import setLengthOfINPUT1_to_Equal_to_INPUT2
from sumManyValue import setLengthOfINPUT2_to_Equal_to_INPUT1
from sumManyValue import CARRY_NUMBER_when_Sum_MoreThan_9
from sumManyValue import OUTPUT_when_Sum_MoreThan_9

class testsumLongValue(unittest.TestCase):

    def test_input_Many_Numbers_Should_Be_Return_Sum_of_theirs(self):
        DATA = [4195838,513922,6893455,7926951,6458072,6748964,5226667,9609279,2630900,6974794,8272865,2338797,3807309,126738,2965130,867810,8952227,7760324,1563304,6846985,235396,9261193,280153,2751168,9805481,6061457,1141236,3374047,697816,6215445,9516472,1203142,9324084,4319819,5621621,3062649,5478301,9353259,8356894,7119733,8382656,7966938,1227218,7479721,6236775,4415335,3064151,2831578,2179736,2495855,6320731,7554101,1185342,4408623,7467911,4194683,6131751,1946829,776830,2412372,2613714,6546567,726731,2341195,3564109,6823646,1200112,6899846,2869356,1295625,3073037,3082505,404013,187316,4093941,2357604,4031349,6580214,919407,3111771,9965068,5234976,7920593,5427652,5595016,8886277,1266609,1526585,7264768,2645033,5169115,3217057,7095403,7666907,9606770,2347090,2358200,8373205,9633590,2999137,2209249,4896248,9297486,726344,6195036,6978117,832705,1538672,3256314,300003,1979643,6229612,2260666,4198801,5881409,5623138,1493468,3180381,4402582,8263225,4147232,4040658,7430206,6426809,7787144,3812014,4716262,1952586,6743933,4145034,6937275,6621551,2331044,2001904,7852328,8149078,7203439,4918218,1481639,7586919,7025268,4780239,1799797,660728,8930335,5454416,9046167]
        EXPECTED_RESULT = "693185264"
        RETURN_RESULT = sumManyValue(DATA)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)
    
    def test_INPUT1_LONG_THAN_INPUT2_AND_INPUT1_SHOULD_NOT_SET(self):
        INPUT1 = "4195838"
        INPUT2 = "513922"
        EXPECTED_RESULT = "4195838"
        RETURN_RESULT = setLengthOfINPUT1_to_Equal_to_INPUT2(INPUT1,INPUT2)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_INPUT1_SHORT_THAN_INPUT2_AND_INPUT1_SHOULD_SET_TO_EQUAL(self):
        INPUT1 = "513922"
        INPUT2 = "4195838"
        EXPECTED_RESULT = "0513922"
        RETURN_RESULT = setLengthOfINPUT1_to_Equal_to_INPUT2(INPUT1,INPUT2)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_INPUT2_LONG_THAN_INPUT1_AND_INPUT2_SHOULD_NOT_SET(self):
        INPUT1 = "513922"
        INPUT2 = "4195838"
        EXPECTED_RESULT = "4195838"
        RETURN_RESULT = setLengthOfINPUT2_to_Equal_to_INPUT1(INPUT1,INPUT2)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

    def test_INPUT2_SHORT_THAN_INPUT1_AND_INPUT2_SHOULD_SET_TO_EQUAL(self):
        INPUT1 = "4195838"
        INPUT2 = "513922"
        EXPECTED_RESULT = "0513922"
        RETURN_RESULT = setLengthOfINPUT2_to_Equal_to_INPUT1(INPUT1,INPUT2)
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

