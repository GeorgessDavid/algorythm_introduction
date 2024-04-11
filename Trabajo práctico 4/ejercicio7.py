""" Leer 10 números enteros e imprimir Su promedio, el mayor valor leído y en
posición se encontraba. Si se ingresó más de una vez sólo debe informar la pri-
mera. """


numeroMasAlto = 0
cantNumeros = 0
registroIngreso = 0
registroMasAlto = 0

while cantNumeros <= 10:
    numero = int(input('\nIngrese un número: \n'))
    if numero > numeroMasAlto:
        numeroMasAlto = numero
        registroMasAlto = registroIngreso
    cantNumeros +=1
    registroIngreso += 1

print('\nEl número ingresado más alto es el: ',numeroMasAlto, 'ingresado en la', registroMasAlto, '° entrada.\n')