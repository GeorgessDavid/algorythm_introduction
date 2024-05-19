'''Escribir un programa para convertir un número binario de 4 cifras en un número
decimal. EI número binario se ingresa como un solo número entero de cuatro
dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente. Este
exponente se obtiene de la posición que ocupa el dígito dentro del número,
comenzando desde la derecha con la posición O. Todos estos resultados se
suman para obtener el valor final. Ejemplo: Convertir 1011 a decimal:
'''

binario = input('Ingrese el número binario de 4 dígitos: ')

d1 = int(binario[0]) * (2 ** 3)
d2 = int(binario[1]) * (2 ** 2)
d3 = int(binario[2]) * (2 ** 1)
d4 = int(binario[3]) * (2 ** 0)

decimal = d1 + d2 + d3 + d4

print('\nEl número es:', decimal, '\n')