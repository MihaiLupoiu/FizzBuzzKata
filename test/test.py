'''
Created on 2/1/2015

@author: myhay
'''
import unittest

from main.FizzBuzz import FizzBuzzIncrementalRange
from main.FizzBuzz import fizzBuzz
from main.FizzBuzz import FizzBuzzRange


resultValue = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 'Fizz', 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Buzz']

class Test(unittest.TestCase):

    def test_3_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(3), "Fizz", "3 check faild")

    def test_5_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(5), "Buzz", "5 check faild")
        
    def test_15_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz", "15 check faild")
    
    def test_31_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(31), "Fizz", "31 check faild")
    
    def test_51_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(52), "Buzz", "52 check faild")
    
    def test_44_OnlyFizzBuzz(self):
        self.assertEqual(fizzBuzz(44), 44, "44 check faild")
    
    def test_vector_FizzBuzz(self):
        self.assertListEqual(FizzBuzzRange([1, 6, 4, 58, 15]), [1, 'Fizz', 4,'Buzz', 'FizzBuzz'], "list check faild")
    
    def test_10_FizzBuzz(self):
        result = FizzBuzzIncrementalRange(1, 10);
        self.assertListEqual(result, resultValue[0:10], "10 check faild")

    def test_15_FizzBuzz(self):
        result = FizzBuzzIncrementalRange(1, 15);
        self.assertListEqual(result, resultValue[0:15], "15 check faild")
        
    def test_30_FizzBuzz(self):
        result = FizzBuzzIncrementalRange(1, 40);
        self.assertListEqual(result, resultValue, "40 check faild")

    def test_100_FizzBuzz(self):
        result = FizzBuzzIncrementalRange(1, 100);
        print result
        
if __name__ == '__main__':
    unittest.main()