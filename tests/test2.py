print("Test 2")
import unittest
import code
import io
import code.getbest

class TestFindTop(unittest.TestCase):
   # def setUp(self):
      #  print("In setup")


    def test_Functio(self):
        print("In testing function")
        number_col =1
        mark_col = 2
        ColData = "ELEN3020,160001,72,OK\nELEN3020,167381,90,Check\n"
        f = io.StringIO(ColData)
        num_index = 0
        mark = 0
        num_index, mark = code.getbest.findTop(f,number_col,mark_col)
        self.assertEqual((num_index,mark),('167381',90))

if __name__=='__main__':
    unittest.main()

