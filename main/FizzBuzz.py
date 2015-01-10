'''
Created on 1/1/2015

@author: myhay
'''

def isFizz(number):
    if  (number%3 == 0) or ("3" in str(number)):
            return True
    return False
    
def isBuzz(number):
    if  (number%5 == 0) or ("5" in str(number)):
            return True
    return False
        
def isFizzBuzz(number):
    if (number %15  == 0):
        return True
    return False

def fizzBuzz(number):
    if (isFizzBuzz(number)):
        return "FizzBuzz"
    elif  (isFizz(number)):
        return "Fizz"
    elif  (isBuzz(number)):
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