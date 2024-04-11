""" Realizar un programa para ingresar desde el teclado un conjunto de números y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un valor -1. """

numero: int(input('\nIngrese un número entero: \n'))
numeroMenor = 0
numeroMayor = 0

while numero != -1: 
    if numero > numeroMayor:
        numeroMayor = numero
    elif numero <= numeroMenor:
        numeroMenor = numero
    else: 
        numeroMenor = numero
        numeroMayor = numero
    numero = int(input('\nIngrese un número entero, para finalizar escriba "-1": \n'))

print('\nEl número mayor ingresado es ', numeroMayor, ' y el número menor es', numeroMenor, '.\n')
