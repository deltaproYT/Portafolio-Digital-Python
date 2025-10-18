import numpy as np
import time

#Declaro Variables
choice = method = None
a1 = b1 = c1 = d1 = a2 = b2 = c2 = d2 = a3 = b3 = c3 = d3 = x = y = z = dtg = dtx = dty = dtz = None 
 

#########################################################################################################################################################################################################################################################################################################################################################################################

print('Bienvenido a la Calculadora de Sistemas de Ecuaciones 3x3')
time.sleep(0.5)

#########################################################################################################################################################################################################################################################################################################################################################################################

time.sleep(0.5)
print(f'\nElija la cantidad de variables: ')

#########################################################################################################################################################################################################################################################################################################################################################################################

time.sleep(0.5)
print(f'Salir | 1\n2 Variables | 2\n3 Variables | 3')

#########################################################################################################################################################################################################################################################################################################################################################################################

def cramereqs2x2(a1,b1,c1,a2,b2,c2):
    try:
        dtg = (a1 * b2) - (a2 * b1)    
        dtx = (c1 * b2) - (c2 * b1)		
        dty = (a1 * c2) - (a2 * c1)
        x = dtx / dtg
        y = dty / dtg
        print(f'Los resultados son\nX = {x}\nY = {y}')
        
    except ZeroDivisionError:
        print('¡ECUACIÓN INVALIDA! No es posible la división entre cero')
    print('Gracias por usar la calculadora!!!\nSystem Shutting Down...')

#########################################################################################################################################################################################################################################################################################################################################################################################


def selection2(ch2): 
    while True:
        if ch2 == 1:
            print('Salio Exitosamente del programa, Su eleccion fue 1') 
            break

        elif ch2 == 2:
            print('Salio Exitosamente del programa, Su eleccion fue 2')
            break

        elif ch2 == 3:
            print('Salio Exitosamente del programa, Su eleccion fue 3')
            break

        else:
            print('Por favor, escoja un valor en la lista de variables: ')
            choices1()
    return ch2

#########################################################################################################################################################################################################################################################################################################################################################################################

def choices1(): #Realiza un bucle donde permite escoger entre 3 valores, para evitar una irrupcion en el codigo se aplica un try-except dentro del bucle donde evalua la excepcion "ValueError" haciendo que sea imposible la continuacion del codigo ingresando un valor incorrezo
    while True:
        try:
            time.sleep(1)
            choice = int(input(f'\nIngrese un valor: '))
            break
        except ValueError:
            time.sleep(1)
            print('Por favor, escoja un valor en la lista de variables: ')
    return choice

#########################################################################################################################################################################################################################################################################################################################################################################################



#########################################################################################################################################################################################################################################################################################################################################################################################

def selection1(ch2): 
    while True:
        if ch2 == 1:
            print('¡Gracias por elegirnos!, salio Exitosamente del programa') 
            break

        elif ch2 == 2:
            print('Ingrese los respectivos valores del sistema de ecuaciones 2x2')
        
            while True:
                try:
                    a1 = int(input('Ingrese el valor de a1: '))
                    b1 = int(input('Ingrese el valor de b1: '))
                    c1 = int(input('Ingrese el valor del termino independiente 1: '))
                    a2 = int(input('Ingrese el valor de a2: '))
                    b2 = int(input('Ingrese el valor de b2: '))
                    c2 = int(input('Ingrese el valor del termino independiente 2: '))
                    break
                except ValueError:
                    print('Por favor, ingrese un valor valido')
            cramereqs2x2(a1,b1,c1,a2,b2,c2)
            break

        elif ch2 == 3:
            print(f'Salir | 1\n2 Metodo Cramer | 2\n3 Gauss Jordan | 3')
            choices1()
            break

        else:
            print('Por favor, escoja un valor en la lista de variables: ')
            choices1()
    return ch2

#########################################################################################################################################################################################################################################################################################################################################################################################








choice = choices1()
selection1(choice)

#x, y, z = cramereqs2x2(x, y, z)
#print(x,y,z)

#print(type(choice))