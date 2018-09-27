import unittest
from sumLongValue import sumLongValue

class testsumLongValue(unittest.TestCase):

    def test_input2Numbers_Should_Be_Return_Sum_of_theirs(self):
        INPUT1 = "341958380513922689345579269516458072674896"
        INPUT2 = "452266679609279263090069747948272865233879"
        EXPECTED_RESULT = "794225060123201952435649017464730937908775"
        RETURN_RESULT = sumLongValue(INPUT1,INPUT2)
        self.assertEqual(RETURN_RESULT, EXPECTED_RESULT)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testsumLongValue)
    unittest.TextTestRunner(verbosity=2).run(suite)

