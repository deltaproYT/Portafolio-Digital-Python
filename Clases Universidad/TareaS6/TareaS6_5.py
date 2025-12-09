import sys
'''
Ejercicio 5 – Números pares en un rango
Solicita un número de inicio y otro de fin.
Muestra todos los números pares comprendidos en ese rango.
'''
pairs = []
odds = []
pares = impares = int()


while True:
    try:
        start = int(input('Por favor ingrese un numero para empezar el rango: '))
        end = int(input('Por Favor ingrese un numero para finalizar el rango: '))
    except ValueError:
        print('por favor escoja un valor valido')
    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()
    break


for i in range(start, end):
    if i % 2 == 0:
        pares += 1
        pairs.append(i)
    else: 
        impares += 1
        odds.append(i)

print(f'Hay un total de {pares} numeros pares y son:\n{pairs}')
print(f'Hay un total de {impares} numeros impares y son:\n{odds}')