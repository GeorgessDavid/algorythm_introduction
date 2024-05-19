'''Un fletero requiere un programa que calcule el precio de sus viajes a partir de la
cantidad de kilómetros que recorre. Para eso cuenta con la siguiente tarifa:
Viaje mínimo $2700. Sólo se cobra cuando el importe por kilómetro no
alcanza este mínimo.
Si recorre entre 0 y 10 km: $400 por km
Si recorre 10 km o más: $200 por km'''

km = float(input('\nIngrese la cantidad de kilómetros a realizar en el viaje:\n'))

costoMinimo = 2700

#validacion
if(km <= 0):
    print('\nLa cantidad de kilómetros introducidos no es válida.\n')
else:
    if(km < 7):
        print('\nEl costo del viaje es de $',costoMinimo,'.\n')
    elif(km > 7 and km <= 10):
        costoMinimo = costoMinimo + (km * 400)
        print('\nEl costo del viaje en relación a recorrer',km,'km es de $',costoMinimo,'.\n')
    else:
        kmRestantes = km - 10
        costoMinimo = costoMinimo + (10 * 400)
        costoMinimo = costoMinimo + (kmRestantes * 200)
        print('\nEl costo del viaje en relación a recorrer',km,'km es de $',costoMinimo,'.\n')