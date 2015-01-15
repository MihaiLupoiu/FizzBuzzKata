'''
Created on 1/1/2015

@author: myhay
'''
lista_factores = [(3,"Fizz"),(5,"Buzz")]

def addFactors(numero,palabra):
    lista_factores.append((numero,palabra))
    
def getListaFactores():
    return lista_factores


def fizzBuzz(numero):
    respuesta = ""
    
    for divisor, respuesta_factor in lista_factores:
        if  (numero%divisor == 0) or (str(divisor) in str(numero)):
            respuesta += respuesta_factor
    
    if (respuesta == ""):
        return numero
    return respuesta


def FizzBuzzRange(lista_numero):
    lista_respuesta = []
    for i in lista_numero:
            lista_respuesta.append(fizzBuzz(i))
    return lista_respuesta

def FizzBuzzIncrementalRange(start, fin):
    lista_respuesta = []
    for i in range(start,fin+1):
            lista_respuesta.append(fizzBuzz(i))
    return lista_respuesta