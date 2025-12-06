'''
Pide al usuario ingresar números indefinidamente. 
El proceso termina cuando se ingresa 0. 
El algoritmo debe calcular y mostrar: 
El promedio de los números positivos 
El promedio de los números negativos 
Usar la estructura Mientras  
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
            sumn = sumn + num
            jmpn = jmpn + 1
        elif num > 0:
            sump = sump + num
            jmpp += 1
        elif num == 0:
            break
    except ValueError:
        print('Por favor ingrese un numero entero')

promn = prom(sumn, jmpn)
promp = prom(sump, jmpp)

print(f'El promedio de los numeros positivos es: {promp}')
print(f'El promedio de los numeros negativos es: {promn}')