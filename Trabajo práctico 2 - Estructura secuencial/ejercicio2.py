'''Desarrollar un programa que permita ingresar dos números enteros A y B a
través del teclado. Imprimir su suma y su diferencia.'''

numeroA = float(input("\nIngrese el primer número:\n"))
numeroB = float(input("\nIngrese el segundo número:\n"))

suma = numeroA + numeroB
resta = numeroA - numeroB

print("Su suma es: ", round(suma,0), "\nSu diferencia es: ", round(resta,0))
