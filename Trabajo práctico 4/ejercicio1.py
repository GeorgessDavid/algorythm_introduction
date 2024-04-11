""" Realizar un programa para ingresar desde el teclado un conjunto de números. Al
finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lec-
tura con -1. """

numeroA = int(input('\nIngrese un número, para finalizar el programa ingrese "-1": \n'))
valorInicial = numeroA
ultimoNumero = 0
while numeroA != -1: 
    numeroPrevio = ultimoNumero
    ultimoNumero = int(input('\nIngrese un número. Para finalizar el programa ingrese "-1": \n'))
    numeroA = ultimoNumero

print('\nEl primer número fue: ', valorInicial, 'y el último número ingresado fue: ',  numeroPrevio, "\n")