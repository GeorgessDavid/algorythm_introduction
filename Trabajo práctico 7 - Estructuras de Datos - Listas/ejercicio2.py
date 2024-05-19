""" Calcular la suma de los números de la lista. """

from ejercicio1 import ingresarNumeros

numbersList = ingresarNumeros(int(input('\nIngrese un número inicial: \n')), int(input('\nIngrese otro número: \n')))

def sumaDeNumerosEnLista(numeros): 
    sumaTotal = 0
    for i in range(len(numeros)):
        sumaTotal += numeros[i]
    
    return sumaTotal

print("\nLa suma total de los números ingresados es de: ", sumaDeNumerosEnLista(numbersList))