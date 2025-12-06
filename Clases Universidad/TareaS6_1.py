import sys
'''
Pide al usuario un número entero y verifica si es primo.
Un número primo solo es divisible entre 1 y él mismo.
Muestra un mensaje informando el resultado.
'''

while True:
    try:
        num = int(input('Por favor ingrese un numero mayor que 1\n'))
        if num <= 1:
            raise ValueError
        break
    except ValueError:
        print('Numero Invalido\n')
        
    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()

def numdiv(num):
    divisors = 0
    for i in range(2, (num - 1)):
        if num % i == 0:
            divisors += 1
    return divisors

if numdiv(num) == 0:
    print('Es un numero primo')

else: 
    print('Es un numero compuesto')

