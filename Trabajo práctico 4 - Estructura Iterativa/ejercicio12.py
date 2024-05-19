'''La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1
Por lo tanto, Fib=0,1,1,2,3,5,8,13,21...
Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de los mismos.'''

fibA = 0
fibB = 1
total = 0

n = int(input('\nIngrese un número: \n'))

while n >= fibB:    
        
        if(total == 1):
                print('\nNúmero: ', total)
        print('\nNúmero: ', total)
        total = fibA + fibB
        fibA = fibB
        fibB = total
        
print('\nLa suma total de los números de la sucesión es de: ', total)