import numpy as np

            
choice = None #Declaro Variables

print('Bienvenido a la Calculadora de Sistemas de Ecuaciones 3x3')
def choices1(): #Realiza un bucle donde permite escoger entre 3 valores, para evitar una irrupcion en el codigo se aplica un try-except dentro del bucle donde evalua la excepcion "ValueError" haciendo que sea imposible la continuacion del codigo ingresando un valor incorrecto
    while True:
        try:
            print(f'Salir | 1\n2 Variables | 2\n3 Variables | 3')
            choice = int(input('Eliga la cantidad de variables: '))
            break
        except ValueError:
            print('Por favor, escoga un valor en la lista de variables')


def choices2(ch2): 

    if ch2 == 1:
        print('Salio Exitosamente del programa, Su eleccion fue 1')

    elif ch2 == 2:
        print('Salio Exitosamente del programa, Su eleccion fue 2')

    elif ch2 == 3:
        print('Salio Exitosamente del programa, Su eleccion fue 3')

    else:
        print('Salio Exitosamente del programa, Su eleccion fue invalida')

choices1()
choices2(choice)
        

#print(type(choice))