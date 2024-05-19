""" Desarrollar un programa que imprima la suma de las números impares comprendidos entre 42 y 176. """

numeroA = 42
numeroB = 176

n = numeroA + 1

sumaNumeros = 0

while n <= numeroB:
    if n % 2 != 0:
        sumaNumeros = n + sumaNumeros

        print('\nValor de N: ', n,  '\n')
        n +=1
    else: 
        n+=1
print('\nLa suma total de los números es de: ', n, '\n')