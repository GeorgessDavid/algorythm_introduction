""" El factorial de un número entero N mayor que cero se define como el producto
de todos los enteros X tales que O < X <= N. Desarrollar un programa para cal-
cular el factorial de un número dado. Deberán rechazarse las entradas inválidas
(menores que O). """


numeroN = int(input('\nIngresar un número entero: \n'))

acumulador_factorial = 0

resultado = 1

while acumulador_factorial != numeroN and numeroN > 0:
    acumulador_factorial += 1
    resultado = resultado * acumulador_factorial

if numeroN > 0:
    print('\nResultaod: ' + resultado)
    