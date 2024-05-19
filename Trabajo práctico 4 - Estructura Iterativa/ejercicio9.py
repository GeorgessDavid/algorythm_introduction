""" Se desea analizar cuántos autos circulan con patente con numeración par y
cuántos con numeración impar en un día. Escribir un programa que permita ingresar
la terminación de la patente (entre O y 9) hasta ingresar -1 e informe
cuántos vehículos pasaron con numeración par y cuántos con numeración impar. """

patentesConNumeroPar = 0
patentesConNumeroImpar = 0

patente = 0

while patente != -1:
    patente = int(input('\nIngresar los tres dígitos de la patente: \n'))

    if patente % 2 == 0:
        patentesConNumeroPar += 1
    else:
        patentesConNumeroImpar +=1

print('\nEn el día circularon ', patentesConNumeroPar, ' patentes pares y ',patentesConNumeroImpar, ' patentes impares.')