'''Una inmobiliaria paga a sus vendedores un salario de $250000, más una comi-
sión de $50000 por cada venta realizada, más el 5% del valor de las ventas.
Realizar un programa que imprima el número del vendedor y el salario que le
corresponde en un determinado mes. Se leen el número del vendedor, la canti-
dad de ventas que realizó y el valor total de las mismas.'''
vendedor = int(input('Introduzca el número del vendedor: \n'))
ventas = int(input('Introduzca la cantidad de ventas que realizó este mes: \n'))
venta = int(input('Introduzca el valor total de las propiedades vendidas: \n'))

salario = 250000
comisiones = 50000 * ventas
valorIndividual = venta / ventas
comision_individual = valorIndividual * 0.05
comision_total = comision_individual * ventas

salarioFinal = salario + comisiones + comision_total

print("\n_______________\n\nSalario inicial: $ 250000 \nComisiones: $", comisiones, "\nComisión del 5% por venta: $", comision_total, "\n________ \n\nEl salario total de ", vendedor, " es de $", round(salarioFinal,2))

