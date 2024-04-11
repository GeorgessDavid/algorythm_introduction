""" Ingresar números, hasta que la suma de los números pares supere 100. Mostrar
cuántos números se ingresaron en total. """

numerosIngresados = 0
sumaDePares = 0
ultimoPar = 0

while sumaDePares <= 100:
    numero = int(input('\nIngrese un número entero: \n'))
    if numero % 2 == 0:
        sumaDePares = ultimoPar + numero
        ultimoPar = numero
    numerosIngresados += 1

print('\nLa suma de los números pares que se ingresaron es de ', sumaDePares, 'y se ingresaron un total de ', numerosIngresados, 'números.\n')