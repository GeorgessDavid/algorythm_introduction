'''Calcular el descuento y el importe a pagar por un medicamento adquirido en una
farmacia. EI precio del mismo se ingresa por teclado. La farmacia realiza un des-
cuento del 35% a todos los medicamentos. Se solicita mostrar el precio original,
el monto del descuento y el importe final a pagar'''

valor = int(input("Ingrese el precio del medicamento: \n")), 
descuento = int(input("Ingrese el % de descuento del medicamento. Sólo números: \n"))

discount = valor * (descuento / 100)

importeTotal = valor - discount

print("\n Medicamento: $", valor, "\n", "Descuento del", descuento, "%: -$", discount, "\n", "Total a abonar: ", importeTotal, "\n")