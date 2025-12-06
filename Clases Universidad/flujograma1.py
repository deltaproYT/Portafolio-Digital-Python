'''
Algoritmo SumaNumerosPositivos
 Definir num, suma Como Real
 suma <- 0
 Escribir "Ingrese un número (negativo para terminar):"
 Leer num
 Mientras num >= 0 Hacer
 suma <- suma + num
 Escribir "Ingrese otro número (negativo para terminar):"
 Leer num
 FinMientras
 Escribir "La suma total de los números ingresados es: ", suma
FinAlgoritmo
'''

suma = 0
while True:
    try:
        num = float(input('Ingrese un número (negativo para terminar):'))
        break
    except ValueError:
        print('Por favor, ingrese un numero')

while num >= 0:
    try:
        suma = suma + num
        num = float(input('Ingrese otro número (negativo para terminar):'))
    except ValueError:
        print('Por favor, ingrese un numero')
print(f'La suma total de los números ingresados es: {suma}')