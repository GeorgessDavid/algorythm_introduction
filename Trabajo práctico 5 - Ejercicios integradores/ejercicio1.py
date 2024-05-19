""" Leer números que representan edades de un grupo de personas, finalizando la
lectura cuando se ingrese eI número -1. Imprimir cuántos son menores de 18
años, cuántos tienen 18 años o más y eI promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válida una
edad y """

mayoresDe18 = 0
menoresDe18 = 0

mayor18=0
menor18=0

ingresarEdad = int(input('\nIngrese la edad: \n' ))

while ingresarEdad != -1 and ingresarEdad < 0:
    
    if ingresarEdad >= 18:
        mayoresDe18 +=1
        mayor18+= ingresarEdad
    else:
        menoresDe18 +=1
        menor18 += ingresarEdad

print('\nLa cantidad de mayores de 18 años es de: ', mayoresDe18, ' y el promedio de edad es de:', mayor18/mayoresDe18)
print('\nLa cantidad de menores de 18 años es de: ', menoresDe18, ' y el promedio de edad es de:', menor18/menoresDe18)