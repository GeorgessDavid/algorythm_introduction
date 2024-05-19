""" Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores. Fi-
nalizar la lectura de datos con -1. """
numero = int(input('\nIngrese un número. Para terminar escriba "-1": \n'))
par = True

while numero != -1:
    if(par == True):
        par = False
    else: 
        par = True
    numero = int(input('\nIngrese un número. Para finalizar escriba "-1": \n'))

if par:
    print('\nLa cantidad de números ingresados es de números ingresados es par.\n')
else:
    print('\nLa cantidad de números ingresados es de números ingresados es impar.\n')