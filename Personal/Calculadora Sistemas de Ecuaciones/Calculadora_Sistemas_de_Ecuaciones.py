import numpy as np
import time

#Declaro Variables
choice = None
a1 = b1 = c1 = d1 = a2 = b2 = c2 = d2 = a3 = b3 = c3 = d3 = x = y = z = dtg = dtx = dty = dtz = None 
 

print('Bienvenido a la Calculadora de Sistemas de Ecuaciones 3x3')
time.sleep(1)
#########################################################################################################################################################################################################################################################################################################################################################################################
print(f'Salir | 1\n2 Variables | 2\n3 Variables | 3')

def choices1(): #Realiza un bucle donde permite escoger entre 3 valores, para evitar una irrupcion en el codigo se aplica un try-except dentro del bucle donde evalua la excepcion "ValueError" haciendo que sea imposible la continuacion del codigo ingresando un valor incorrezo
    while True:
        try:
            time.sleep(1)
            choice = int(input(f'\nElija la cantidad de variables: '))
            break
        except ValueError:
            time.sleep(1)
            print('Por favor, escoja un valor en la lista de variables: ')
    return choice
#########################################################################################################################################################################################################################################################################################################################################################################################

def selezion(ch2): 
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

def cramereqs2x2(a1,b1,c1,a2,b2,c2):
    dtg = (a1 * b2) - (a2 * b1)    
    dtx = (c1 * b2) - (c2 * b1)		
    dty = (a1 * c2) - (a2 * c1)
    x = dtx / dtg
    y = dty / dtg
    return x, y, z




choice = choices1()
selezion(choice)

x, y, z = cramereqs2x2(x, y, z)
print(x,y,z)

#print(type(choice))