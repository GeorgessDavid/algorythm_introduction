nombreInstrumento = 0
cantidadDeStock = 0
precioDelInstrumento = 0

instrumentoMasCaroValor = 0
instrumentoMasBaratoValor = False
instrumentoConMasStock = 0
instrumentoConMenosStock = False

precios = 0
cantidadDeInstrumentos = 0
instrumentosDisponibles = 0

nombreMasCaro = 0
nombreMasBarato = 0
nombreMasStock = 0
nombreMenosStock = 0

while nombreInstrumento != "fin":
    nombreInstrumento = input('\nIngrese el nombre del instrumento:\n')
    if nombreInstrumento != "fin":        
        cantidadDeStock = int(input('\nIngrese el stock del mismo:\n'))
        precioDelInstrumento = float(input('\nIngrese el valor del instrumento: \n'))

        # Definimos cantidad de instrumentos y precios totales.
        cantidadDeInstrumentos +=1
        precios += precioDelInstrumento

        #Si hay stock del instrumento se cuenta para la cantidad de stock
        if cantidadDeStock > 0:
            instrumentosDisponibles += 1

        # Si el instrumento es el que más stock tiene, se lo almacena.
        if instrumentoConMasStock < cantidadDeStock:
            instrumentoConMasStock = cantidadDeStock
            nombreMasStock = nombreInstrumento

        # Si el instrumento es el que menos stock tiene, se lo almacena.
        if instrumentoConMenosStock > cantidadDeStock or instrumentoConMenosStock == False:
            instrumentoConMenosStock = cantidadDeStock
            nombreMenosStock = nombreInstrumento
        


        # Si el precio del instrumento ingresado es mayor que el que ya tenemos con más valor, lo guardamos.
        if precioDelInstrumento > instrumentoMasCaroValor:
            instrumentoMasCaroValor = precioDelInstrumento
            nombreMasCaro = nombreInstrumento

        # Si el precio del instrumento ingresado es menor, se lo guarda.
        if precioDelInstrumento < instrumentoMasBaratoValor or instrumentoMasBaratoValor == False:
            instrumentoMasBaratoValor = precioDelInstrumento
            nombreMasBarato = nombreInstrumento

        if cantidadDeStock < 5:
            print('\n', nombreInstrumento, 'es uno de los instrumentos con menos de 5 unidades en stock.\n')

if(precios != 0 and cantidadDeInstrumentos != 0):
    promedio = precios/cantidadDeInstrumentos
else:
    print('\nDebe ingresar al menos un instrumento.\nReinicie el programa.\n')

print('\nEl instrumento más caro es: \n', nombreMasCaro, 'con un valor de: $', instrumentoMasCaroValor)
print('\nEl instrumento más barato es: \n', nombreMasBarato, 'con un valor de: $', instrumentoMasBaratoValor)
print('\nEl instrumento con más stock es: \n', nombreMasStock)
print('\nEl instrumento con menos stock es: \n', nombreMenosStock)
print('\nEl promedio de precios es de: ', round(promedio))