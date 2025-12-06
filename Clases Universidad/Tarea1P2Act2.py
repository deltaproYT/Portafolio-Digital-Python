import sys
'''
El usuario ingresa un número entero positivo. 
El algoritmo debe encontrar su mayor divisor propio (distinto de él mismo) usando un ciclo REPETIR 
'''

def data_entry():
    while True:
        try:
            num = int(input('Por favor ingrese un numero entero positivo diferente de 1: '))
            if num <= 1:
                raise ValueError() 
            return num
        except ValueError:
            print('Por favor ingrese un valor valido')
        except KeyboardInterrupt:
            print('\nSystem shutting down...') 
            sys.exit()

div = num = data_entry()
while True:
    div -= 1
    if num % div == 0:
        break

print(f'El mayor divisor propio de {num} es {div}')