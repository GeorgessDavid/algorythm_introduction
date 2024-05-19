""" Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la fun-
ción mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si eI usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B. """

def ingresarNumeros(numA, numB):
    numbersList = []

    numeroIngresado = int(input("\nIngrese un número: \n"))

    while numeroIngresado != -1: 

        
        while (numeroIngresado < numA or numeroIngresado > numB) and numeroIngresado != -1:
            numeroIngresado = int(input("\nIngresaste un número fuera de rango, vuelve a ingresarlo: \n"))
            if numeroIngresado == -1:
                return numbersList
    
        numbersList.append(numeroIngresado)

        numeroIngresado = int(input("\nIngrese un número: \n"))
    
    return numbersList
