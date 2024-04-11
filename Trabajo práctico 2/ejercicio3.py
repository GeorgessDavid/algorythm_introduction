'''Calcular el promedio de las notas que obtiene un alumno al rendir los dos
parciales.'''

nombre = input("\nPor favor, ingrese el nombre y apellido del alumno: \n")
nota1 = float(input("\nIngrese la nota del primer parcial: \n"))
nota2 = float(input("\nIngrese la nota del segundo parcial: \n"))

prom = (nota1 + nota2) / 2

print("El promedio del alumno ", nombre, "es:\n", prom)
