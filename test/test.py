'''
Created on 2/1/2015

@author: myhay
'''
import unittest

from main.FizzBuzz import FizzBuzzStage1
from main.FizzBuzz import FizzBuzzStage2

resultValueStage1 = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz' ]
resultValueStage2 = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 'Fizz', 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'Buzz']

class Test(unittest.TestCase):

# Pruebaas de la primera parte

    def test10FizzBuzzStage1(self):
        result = FizzBuzzStage1(1, 10);
        self.assertListEqual(result, resultValueStage1[0:10], "10 check faild")


    def test15FizzBuzzStage1(self):
        result = FizzBuzzStage1(1, 15);
        self.assertListEqual(result, resultValueStage1[0:15], "15 check faild")
        
    def test30FizzBuzzStage1(self):
        result = FizzBuzzStage1(1, 30);
        self.assertListEqual(result, resultValueStage1, "30 check faild")
        
    def test100FizzBuzzStage1(self):
        result = FizzBuzzStage1(1, 100);
        print result

# Pruebaas de la segunda parte

    def test10FizzBuzzStage2(self):
        result = FizzBuzzStage2(1, 10);
        self.assertListEqual(result, resultValueStage2[0:10], "10 check faild")

    def test15FizzBuzzStage2(self):
        result = FizzBuzzStage2(1, 15);
        self.assertListEqual(result, resultValueStage2[0:15], "15 check faild")
        
    def test30FizzBuzzStage2(self):
        result = FizzBuzzStage2(1, 40);
        self.assertListEqual(result, resultValueStage2, "40 check faild")

    def test100FizzBuzzStage2(self):
        result = FizzBuzzStage2(1, 100);
        print result
        
if __name__ == '__main__':
    unittest.main()