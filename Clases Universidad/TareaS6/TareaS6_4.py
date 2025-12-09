import sys
'''
Ejercicio 4 – Factorial
Pide al usuario un número entero positivo y genera su factorial usando un bucle.
Recuerda:
n! = 1 × 2 × 3 × … × n
'''
fact = 1
factmult = []
while True:
    try:
        num = int(input('Por Favor ingrese un numero entero positivo: '))
        if num < 0:
            raise ValueError
        break
    except ValueError:
        print('Por favor ingrese un valor valido')
    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()

for i in range(num):
    fact = fact * (i + 1)
    factmult.append(i+1)

factmult.reverse()
del factmult[0]


print(f'{num}! = {num}', end=" ")
for i in factmult:
    print(f'x {i} ', end="")

print(f'= {fact}')
