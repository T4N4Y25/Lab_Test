Tanay Rangasamy - 2544162

The repository has two main folders: a code and tests folder.
The code folder has the main python program file getbest.py and the tests folder has the unit tests and the csv sample data
The program in the code folder operates by examining the sample data and determining which columns hold the student numbers and which holds the marks
The program then goes through the columns and determines which student got the highest mark. 
To run the code, execute the program along with the sample data.
eg. cd ~/Lab_test
    python3 code/getbest.py tests/bestdat0.csv
The output should return 

The top student was student 167381 with 90

Two tests are included to test methods within the getbest.py program (found in the tests folder).
The first test checks whether the getCol function correctly returns the proper column indexes with sample data within the code.
To run the test: 
cd ~/Lab_Test 
python3 -m unittest tests/test1.py

Similarly the 2nd test checks whether the findTop function correctly identifies the highest mark using sample data within the code.
To run the 2nd test:
cd ~/Lab_Test
python3 -m unittest tests/test2.py
