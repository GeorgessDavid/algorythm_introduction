''' 
Un productor agrícola desea estimar cuántos quintales de trigo puede producir
en su parcela. Escribir un programa para ingresar el largo y el ancho en metros
de la misma y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quinta-
les.'''

long = float(input('\nIntroduzca el largo de la parcela en metros: \n'))
anch = float(input('\nIntroduzca el ancho de la parcela en metros: \n'))

m2totales = long * anch
cantidadQuintales = m2totales / 5
print('\nCon las medidas ingresadas, tenes ', cantidadQuintales, ' quintales en un área de ', m2totales, 'metros cuadrados. \n')