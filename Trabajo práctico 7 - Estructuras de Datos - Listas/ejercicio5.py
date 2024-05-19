""" Desarrollar una función que reciba la lista como parámetro y devuelva una nueva
lista con los mismos elementos de la primera, pero en orden inverso. Por
ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5]. """

from ejercicio1 import ingresarNumeros

numbersList = ingresarNumeros(int(input('\nIngrese un número inicial: \n')), int(input('\nIngrese un número final: \n')))

def deReversaMami(list):
    listaRevertida = []

    for i in range(len(list)-1, -1, -1):
        listaRevertida.append(list[i])
    return listaRevertida

print(deReversaMami(numbersList))