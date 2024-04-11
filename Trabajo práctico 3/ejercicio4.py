'''En el congreso se vota una ley muy importante. Desarrollar un programa que
permita ingresar la cantidad de votos a favor y en contra, e informe el porcenta-
je obtenido en cada caso y si la misma fue aprobada o no.'''

favor = int(input("\nIntroduzca la cantidad de votos a favor: \n"))
contra = int(input("\nIntroduzca la cantidad de votos en contra: \n"))
votosTotales = favor + contra
porcentajeFavor = (favor * 100) / votosTotales
porcentajeEnContra = 100 - porcentajeFavor

if(favor > contra):
    print('\nLa ley se ha aprobado con el ', round(porcentajeFavor,2), '% de votos a favor.\n')
elif(favor ==contra):
    print('\nHa ocurrido un error, existen la misma cantidad de votos a favor y en contra.\n')
else:
    print('\nLa ley ha sido rechazada con un ', round(porcentajeEnContra,2), '% de votos en contra.\n')