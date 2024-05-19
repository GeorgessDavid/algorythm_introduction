from ejercicio1 import ingresarNumeros

numbersList = ingresarNumeros(int(input('\nIngrese un número inicial: \n')), int(input('\nIngrese un número final: \n')))

def isPalindrome(numeros):
    reversedNumbers = []

    for i in range(len(numeros)-1, -1, -1):
        reversedNumbers.append(numeros[i])
    
    if numeros == reversedNumbers:
        return True
    else:
        return False

esPalindromo = isPalindrome(numbersList)

result = '\nLa lista es capicúa. \n' if esPalindromo == True else '\nLa lista no es capicúa. \n'

print(result)
