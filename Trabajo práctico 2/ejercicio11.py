''' Leer un período en segundos e imprimirlo expresado en días, horas, minutos y
segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minu-
tos y 20 segundos.'''

seconds = int(input('Ingrese la cantidad de segundos: '))

dia = seconds // (24 * 3600)
segundos_sobran = seconds % (24 * 3600)
horas = segundos_sobran // 3600
segundos_sobran %= 3600
minutos = segundos_sobran // 60
segundos_sobran %= 60
segundos = segundos_sobran

print('\n',seconds, 'segundos en el sistema hexadecimal son ', dia, 'días ', horas, 'horas ', minutos, 'minutos y ', segundos, 'segundos.\n')