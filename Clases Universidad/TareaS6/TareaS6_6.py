from random import randint
import sys
'''
Ejercicio 6 – Adivina el número
Genera un número aleatorio entre 1 y 100.
El usuario debe intentar adivinarlo.
Indicar si el intento está muy alto o muy bajo hasta que acierte.
Requiere import random.
'''

randnum = randint(0, 100)

while True:
    try:
        inpnum = int(input('Adivine el numero entero del 1 al 100: '))
        if inpnum > randnum:
            print('Muy Alto')
        elif inpnum < randnum:
            print('Muy Bajo')
        else:
            print(f'Adivinasteeeeeee el numero era {randnum}!!!')
            break
    except ValueError:
        print('por favor escoja un valor valido')
    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()