import sys
'''
Ejercicio 10 – Número perfecto
Pide un número entero y determina si es perfecto.
Un número perfecto es igual a la suma de sus divisores propios.
Ejemplo: 6 → 1 + 2 + 3 = 6
'''
sumdiv = 0
while True:
    try:
        num = int(input('Por favor ingrese un numero entero: '))
        break
    except ValueError:
        print('Por favor ingrese un valor valido')
    except KeyboardInterrupt:
        print('System Shutting Down...')
        sys.exit()


for i in range(1 ,num):
    if num % i == 0:
        sumdiv += i

print(sumdiv)
if sumdiv == num:
    print(f'El numero {num} es un Numero Perfecto')

else:
    print(f'El numero {num} es un NO es Numero Perfecto')