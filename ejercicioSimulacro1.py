"""
b) El programa recibe un número.
Ese número lo guarda.
Al recibir el siguiente número. Suma el nuevo número al número guardado.
Al recibir un total de 10 números, este finaliza y calcula el promedio total 
de los números ingresados y lo muestra por pantalla. 

c) Los datos de entrada serían los números que ingresan a través del teclado. 
El dato de salida sería el promedio de los números.

d) Las variables declaradas son: 
    'contador' es la variable que establece la cantidad máxima de números a ingresar,
    en este caso 10. 
        Este tipo de dato es un número entero.
    'suma' es la variable que, inicialmente guarda el número ingresado, 
    luego del primer número recibe el resultado de la suma del mismo con el número
    ingresado. 
        El tipo de dato de la suma es un tipo float.
    'numero' es la variable que recibe el número ingresado por el teclado.
    'promedio' es la variable que contiene el resultado del promedio de la suma de 
    los números ingresados.

e) En el diagrama de flujo se visualiza el resultado en la salida previa 
al fin del programa.

    
"""
LIMITE = 10
contador = 0
suma = 0

while contador < LIMITE:
    numero = float(input('Ingresar número:'))
    suma += numero
    contador +=1

promedio = suma/LIMITE

print('El promedio de los números es: ', promedio)