'''
Created on 1/1/2015

@author: myhay
'''

#Implementacion del fizzBuzz solo si es divisible por 3, 5 o 15 (Fizz, Buzz o FizzBUuzz)
def FizzBuzzStage1(start, fin):
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

#Implementacion del fizzBuzz que si es divisible por 3, 5 o 15 sustituye su valor por Fizz, Buzz o FizzBuzz respectivamente.
#Ademas si el numero contiene el valor 3 aparece Fizz y si el numero contiene 5 aparece Buzz.
#La implmentacion se utilizo tal cual se explica en el ejemplo. 
#Eso significa que si aparece el numero 53 por ejemplo, el resultado sera Fizz y no Buzz, dado que la cadena contiene un 3 y este valor se comprueba antes que el 5.
def FizzBuzzStage2(start, fin):
    result = []
    for i in range(start,fin+1):
        if (i%15  == 0):
            result.append("FizzBuzz")
        elif  (i%3 == 0) or ("3" in str(i)):
            result.append("Fizz")
        elif  (i%5 == 0) or ("5" in str(i)):
            result.append("Buzz")
        else:
            result.append(i)
    return result

print FizzBuzzStage1(1, 100);
print FizzBuzzStage2(1, 100);