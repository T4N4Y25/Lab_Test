print("Test One")
import unittest
import sys
import os
import io
from code import getbest

class TestColumnMethod(unittest.TestCase):
    def test_col1(self):
        print("Testing columns")
        number_col2 = 2
        mark_col2 = 3
        ColData = "Course,Student Number,Mark,Comment"
        number_col2, mark_col2 = getbest.getCols(ColData)
        self.assertEqual((number_col2,mark_col2),(2,3))

if __name__ == '__main__':
    unittest.main()



