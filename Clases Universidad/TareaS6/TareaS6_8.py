import sys
'''
Ejercicio 8 – Promedio de notas
El usuario ingresará notas entre 0 y 10.
El programa termina cuando se ingrese -1.
Calcular el promedio de las notas válidas ingresadas.
'''
califtotal = jump = 0
notas = []

def converttype(num):
    if num.is_integer():
        return int(num)
    else:
        return num

while True:
    try:
        calif = float(input('Por favor ingrese una calificacion: '))

        if ((calif < 0) and (calif != -1)) or (calif > 10):
            raise ValueError
        if calif == -1:
            break
        jump +=1
        califtotal += calif
        notas.append(converttype(calif))
        califprom = califtotal / jump
        califprom = converttype(califprom)
    except ValueError:
        print('Por favor ingrese un valor valid\n')
    except KeyboardInterrupt:
        print('\nSystem shutting down...') 
        sys.exit()

print(f'El promedio de las notas {notas}\nes: {califprom}')


