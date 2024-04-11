'''Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y
estado civil (1 si es soltero o 2 si es casado). Se debe informar: (reemplazar los
9 por los valores que correspondan)'''
sueldoBasico = float(input("\nIngrese el sueldo básico del empleado: \n"))
estadoCivil = int(input("\nIngrese el estado civil del empleado. (1 si es soltero, 2 si es casado): \n"))
antiguedad = int(input("\nIngrese los años de antigüedad del empleado: \n"))


sueldoNeto = sueldoBasico
Antiguedad = 0
    
if(estadoCivil != 1 or estadoCivil != 2):
    print('\nIngresaste un estado civil inválido.\n')
else:
    if(estadoCivil == 1):
        Antiguedad = (sueldoBasico  * 0.05 * antiguedad)
        sueldoNeto = sueldoBasico + Antiguedad
    else:
        Antiguedad =  (sueldoBasico * 0.07 * antiguedad)
        sueldoNeto = sueldoBasico + Antiguedad
    jubilacion = sueldoNeto * 0.11
    obraSocial = sueldoNeto * 0.03
    indicato = sueldoNeto * 0.03
    
    sueldoNeto = sueldoNeto - jubilacion - obraSocial - indicato
    print("\nSueldo Básico: \n", sueldoBasico)
    print("\nDescuentos: \n")
    print("Antigüedad: ", antiguedad, "años. +$",Antiguedad )
    print("Jubilación: -$",jubilacion)
    print("Obra social: -$", obraSocial)
    print("Sindicato: -$", indicato)
    print("\n\nSueldo Neto: $", sueldoNeto)