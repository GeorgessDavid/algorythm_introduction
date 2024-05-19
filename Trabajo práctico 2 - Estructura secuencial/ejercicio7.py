''' Una persona invierte su capital en un banco y desea saber cuánto dinero ganará
en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará
en seis meses si deja su dinero invertido? '''
inversionInicial = float(input("Ingrese el monto a invertir: \n"))
meses = int(input("Ingrese el plazo en cantidad de meses: \n"))

tasaMensual = 0.02  

montoFinal = inversionInicial * (1 + tasaMensual) ** meses
gananciaNeta = montoFinal - inversionInicial

print('\nLa ganancia final en el lapso de', meses, 'meses es de: $', round(gananciaNeta, 2), '\nEl total del dinero ahora es de: $', round(montoFinal, 2), "\n")
