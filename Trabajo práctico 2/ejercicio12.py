'''
Un banco necesita para sus cajeros automáticos un programa que lea una
cantidad de dinero e imprima a cuántos billetes equivale, considerando que
existen billetes de $IOOO, $500, $IOO, $50, $IO, $5 y $1. Desarrollar dicho
programa de tal forma que se minimice la cantidad de billetes entregados por el
cajero.
'''

cash = int(input('\nIntroduzca la cantidad entera de dinero a imprimir: '))

billetesDeMil = cash // 1000
billetesRestantes = cash % 1000
billetesDe500 = billetesRestantes // 500
billetesRestantes %= 500
billetesDe100 = billetesRestantes // 100
billetesRestantes %= 100
billetesDe50 = billetesRestantes // 50
billetesRestantes %= 50
billetesDe10 = billetesRestantes // 10
billetesRestantes %= 10
billetesDe5 = billetesRestantes // 5
billetesRestantes %= 5
billetesDe1 = billetesRestantes

print('\n La mejor forma de imprimir los billetes es de la siguiente manera: \n', billetesDeMil, 'billetes de $1000\n', billetesDe500,'billetes de $500\n', billetesDe100, 'billetes de $100\n', billetesDe50, 'billetes de $50\n', billetesDe10,'billetes de $10\n',billetesDe5,'billetes de $5\nY por último', billetesDe1,'billetes de $1\n')
