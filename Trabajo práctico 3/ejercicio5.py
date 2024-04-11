'''Ingresar las notas de los dos parciales de un alumno e indicar si promocionó,
aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está
entre O y 10.
Se promociona cuando las notas de ambos parciales son mayores 0
iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales
Se debe recuperar cuando al menos una de las dos notas es menor a 4.'''

nota1= int(input("\nIngrese la nota del primer parcial: \n"))
nota2= int(input("\nIngrese la nota del segundo parcial: \n"))
if (nota1> 10 or nota2 > 10 or nota1 <= 0 or nota2 <=0):
    print('Ha ocurrido un error, alguna de las notas no son válidas.')
elif (nota1 >= 7 and nota2 >= 7):
    print('El alumno aprobó y promocionó la materia.')
elif (nota1 >= 4 and nota2 >= 4):
    print('El alumno aprobó la materia.')
else:
    if(nota1 < 4):
        print('El alumno desaprobó la materia, deberá recuperar el primer parcial.')
    else: 
        print('El alumno desaprobó la materia, deberá recuperar el segundo parcial.')