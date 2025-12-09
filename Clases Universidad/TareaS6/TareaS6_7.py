import sys
'''
Ejercicio 7 – Serie Fibonacci
Pide un número entero n y muestra los primeros n términos de la serie Fibonacci.
Ejemplo: 0, 1, 1, 2, 3, 5…
'''

fibonacci = [0,1]
while True:
    try:
        jump = int(input('Por favor, ingrese un numero de saltos para la serie de fibonacci: '))
        if jump <= 0:
            raise ValueError
        break
    except ValueError:
        print('Por favor escoja un numero mayor que 0')

    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()



for i in range(1, (jump -1)):
    nofibo = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(nofibo)


    
print(f'Los primeros {jump} numeros de la sucesion de fibonacci son:\n0\n1')
for i in range(2, (jump)):
    print(f'{fibonacci[i-2]} + {fibonacci[i - 1]} = {fibonacci[i]}')



