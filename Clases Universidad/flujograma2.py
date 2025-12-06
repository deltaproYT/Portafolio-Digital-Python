'''
Diseña un algoritmo que pida al usuario ingresar números de forma indefinida. 
El proceso debe terminar cuando el usuario ingrese un número negativo. 
Finalmente, el programa debe calcular y mostrar el promedio de los números positivos 
ingresados. 
'''

sumn = jmpn = sump = jmpp = num = 0

def prom(sum,total):
    try:
        prom = sum/total
        return prom
    except ZeroDivisionError:
        return ('No hay numeros')

        


while True:  
    try:            
        num = int(input(r'Por favor ingrese un numero: '))
        if num < 0:
            break
        elif num >= 0:
            sump = sump + num
            jmpp += 1
        
    except ValueError:
        print('Por favor ingrese un numero entero')

promp = prom(sump, jmpp)

print(f'El promedio de los numeros positivos es: {promp}')