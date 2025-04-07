print("Test 2")
import unittest
import code
import io

class TestFindTop(unittest.TestCase):
   # def setUp(self):
      #  print("In setup")


    def test_Functio(self):
        print("In testing function")
        number_col =1  #Set the indexes that getCol would've gotten
        mark_col = 2
        ColData = "ELEN3020,160001,72,OK\nELEN3020,167381,90,Check\n" #Simple test string
        f = io.StringIO(ColData)
        num_index = 0
        mark = 0
        num_index, mark = code.getbest.findTop(f,number_col,mark_col) #Run the findTop function
        self.assertEqual((num_index,mark),('167381',90)) #See if the function returns the correct expected value

if __name__=='__main__':
    unittest.main()

