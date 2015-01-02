'''
Created on 2/1/2015

@author: myhay
'''
import unittest
from main.FizzBuzz import FizzBuzz

resultValue = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz' ]

class Test(unittest.TestCase):

    def test10FizzBuzz(self):
        result = FizzBuzz(1, 10);
        self.assertListEqual(result, resultValue[0:10], "10 check faild")


    def test15FizzBuzz(self):
        result = FizzBuzz(1, 15);
        self.assertListEqual(result, resultValue[0:15], "15 check faild")
        
    def test30FizzBuzz(self):
        result = FizzBuzz(1, 30);
        self.assertListEqual(result, resultValue, "30 check faild")
        
    def test100FizzBuzz(self):
        result = FizzBuzz(1, 100);
        print result

if __name__ == '__main__':
    unittest.main()