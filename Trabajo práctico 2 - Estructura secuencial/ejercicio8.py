'''Leer una medida en metros e imprimir esta medida expresada en centímetros,
pulgadas, pies y yardas. Los factores de conversión son:
1 pie 12 pulgadas
I yarda = 3 pies
1 pulgada 2,54 cm.
1 metro 100 cm.'''

metros = float(input('Ingrese la cantidad de metros a invertir, recuerde que los decimales deben expresarse con . en vez de , : \n'))

pulgada = 0.0254
pie = pulgada * 12
yarda = pie * 3
centimetros = 100

print('\n La medida en pulgadas es de: ', round((metros*pulgada), 2), " pulgadas. \n La medida en pies es de: ", round((metros*pie),2), 'pies. \n La medida en yardas es de: ', round((metros*yarda),2), ' yardas. \n La medida en centímetros es de: ', round((metros*centimetros),2), 'centímetros. \n')

