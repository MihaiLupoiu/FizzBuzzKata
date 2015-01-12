'''
Created on 1/1/2015

@author: myhay
'''

def fizzBuzz(number):
    if (number %15  == 0):
        return "FizzBuzz"
    elif  (number%3 == 0) or ("3" in str(number)):
        return "Fizz"
    elif  (number%5 == 0) or ("5" in str(number)):
        return "Buzz"
    else:
        return number


def FizzBuzzRange(lista):
    result = []
    for i in lista:
            result.append(fizzBuzz(i))
    return result

def FizzBuzzIncrementalRange(start, fin):
    result = []
    for i in range(start,fin+1):
            result.append(fizzBuzz(i))
    return result