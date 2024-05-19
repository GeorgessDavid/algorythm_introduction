'''Desarrollar un programa que solicite un número de mes (por ejemplo 4) y
escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y
mostrar un mensaje de error en caso de que no 10 sea.'''

numero = int(input("\nIngrese el número del mes: "))

if(numero == 4):
    print("\nAbril\n")
elif((numero <= 3 and numero >=1) or (numero >=5 and numero <= 12)):
    print('\nIngresaste un mes válido, pero no es el mes de abril.\n')
else:
    print('\nEl número que ingresaste no es válido.\n')