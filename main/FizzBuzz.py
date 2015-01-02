'''
Created on 1/1/2015

@author: myhay
'''

def FizzBuzz(start, fin):
    result = []
    for i in range(start,fin+1):
        if (i%15  == 0):
            result.append("FizzBuzz")
        elif (i%3 == 0):
            result.append("Fizz")
        elif (i%5 == 0):
            result.append("Buzz")
        else:
            result.append(i)
    return result