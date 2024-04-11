'''Tres personas aportan dinero para fundar una empresa (no necesariamente en
partes iguales). Calcular qué porcentaje invirtió cada una.'''
persona1=int(input("\n Ingrese el monto de la inversión del primer inversor: "))
persona2=int(input("\n Ahora ingrese el monto del segundo inversor: "))
persona3=int(input("\n Por último, ingrese el monto del último inversor: "))

total = persona1 + persona2 + persona3

aporte_persona1 = (100 * persona1) /  total
aporte_persona2 = (100 * persona2) /  total
aporte_persona3 = (100 * persona3) /  total

print("\n La persona que aportó $",persona1, ", aportó un ",round(aporte_persona1, 2), "% del total. \n", "La persona que aportó $", persona2, ", aportó un ",round(aporte_persona2,2),"% del total. \n", "La persona que aportó $", persona3, ", aportó un ", round(aporte_persona3,2), "% del total. \n")