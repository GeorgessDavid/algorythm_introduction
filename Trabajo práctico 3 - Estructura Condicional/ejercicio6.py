'''Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. EI costo básico del libro es de $5000, más $32 por página con encua-
dernación rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $1200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-
cuadernación que incrementa el costo en otros $3360. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas.'''
paginas = int(input('\nIngrese la cantidad de páginas que contiene el libro: \n'))

libro = 5000
costoTotal = libro + (paginas * 32)
valorPaginas = paginas * 32

if(paginas >= 600):
    print("\nLibro base: $5000\nPáginas x",paginas,": $",valorPaginas)
    costoTotal = costoTotal + 1200 + 3360
    print("Adicional por más de 300 páginas: $1200")
    print("Adicional por más de 600 páginas: $3360")
elif(paginas >= 300):
    print("\nLibro base: $5000\nPáginas x",paginas,": $",valorPaginas)
    costoTotal = costoTotal + 1200
    print("Adicional por más de 300 páginas: $1200")
else: 
    print("\nLibro base: $5000\nPáginas x",paginas,": $",valorPaginas)    

print("\nEl costo total del libro es de $", costoTotal, "\n")