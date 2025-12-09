import sys
'''
Ejercicio 2 – Tabla de multiplicar
Pide un número y muestra su tabla de multiplicar del 1 al 10.
Formato sugerido:
n x i = resultado
'''
prod = float()

def converttype(num):
    strnum = str(num)
    if '.' in strnum:
        return float(num)
    else:
        return int(num)

while True:
    try:
        num = input('Por favor ingrese un numero: ')
        num = converttype(num)
        break
    except ValueError:
        print('Por favor ingrese un valor valido\n')
    except KeyboardInterrupt:
            print('\nSystem shutting down...') 
            sys.exit()

print(f'la tabla del {num} es:\n')
for i in range(10):
    prod = (i + 1) * num
    print(f'{num} x {i+1} = {prod}')