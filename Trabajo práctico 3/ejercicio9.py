'''Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no.'''
dia = int(input('\nIngrese un día: \n'))
mes = int(input('\nIngrese un mes: \n'))
year= int(input('\nIngrese un año: \n'))

if dia < 0 or dia > 31: 
    print('\nIngresaste un día inválido.\n')
elif mes == 2 and (dia < 0 or dia > 29):
    print('\nIngresaste un día inválido.\n')
elif mes < 0 or mes >12:
    print('\nIngresaste un mes inválido.\n')
else:
    print('\nEl día y el mes que ingresaste es válido.\n')