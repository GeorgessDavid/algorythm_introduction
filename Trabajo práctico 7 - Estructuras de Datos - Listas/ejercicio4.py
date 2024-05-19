""" 
Escribir una función para contar cuántas veces aparece un valor dentro de la
lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
un número entero.

"""
from ejercicio1 import ingresarNumeros

numbersList = ingresarNumeros(int(input('\nIngrese un número inicial: \n')), int(input('\nIngrese un número final: \n')))

def contarNumeros(list, toFind):
    numerosEnLista = 0

    for i in range(len(list)):
        if list[i] == toFind:
            numerosEnLista += 1
    
    return numerosEnLista

numeroToFind = int(input('\nIngrese el número entero a buscar:\n'))

print("\nSe encontraron un total de ",contarNumeros(numbersList, numeroToFind), "números.\n")
