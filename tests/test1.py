print("Test One")
import unittest
import io 
import code #Folder containing getbest.py, the __init__.py file has details on the import

class TestColumnMethod(unittest.TestCase):
    def test_col1(self):
        print("Testing columns")
        number_col2 = -1
        mark_col2 = -1
        ColData = "Course,Student Number,Mark,Comment"
       # f = open(sys.argv[1])
        f = io.StringIO(ColData) #Puts test string in a csv file-type format
        number_col2, mark_col2 = code.getbest.getCols(f) #store the results of the function from the test string
        self.assertEqual((number_col2,mark_col2),(1,2)) #Compare the results to expected results

if __name__ == '__main__':
    unittest.main()



