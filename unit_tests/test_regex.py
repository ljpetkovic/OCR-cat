import unittest, os, warnings
from corr_trans_ALTO import closed_i


TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "1855_08_LAC_N72_0002_line.xml_trans.xml")

test_input_1="en Grèce. <i>L. a. s</i>/i, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,"
test_result_1="en Grèce. <i>L. a. s</i>, à Barbié du Bocage, Paris, 1806, 1 p. 1/4,"

##### Test each assertion previously defined

class TestClosed(unittest.TestCase):

    def setUp(self):
        with open(TESTDATA_FILENAME) as self.testfile:
            self.testdata = self.testfile.read()
            warnings.simplefilter('ignore', ResourceWarning)
       
    def test_closed_i(self):
        self.assertEqual(closed_i(test_input_1), test_result_1)
    
if __name__ == '__main__':
    unittest.main()



