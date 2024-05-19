""" Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar? """

n = 1
multiplicarPor = int(input('\nIngrese el número entero por cuál multiplicar: \n'))
resultadoMultiplicacion = 0

while n <= 12:
    resultadoMultiplicacion = n * multiplicarPor
    print('\n', n, 'x', multiplicarPor, '=', resultadoMultiplicacion,'\n')
    n+=1
