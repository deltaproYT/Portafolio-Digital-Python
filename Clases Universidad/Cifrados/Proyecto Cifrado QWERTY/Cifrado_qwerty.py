import Cifrado_QWERTY_fun as cqf
lista = []

# Ingrese la tabla en la que esta escrito el mensaje a cifrar
while True:
    try:
        n = int(input('Ingrese el numero de distribucion en el que esta la palabra: '))
         
        if ((n>0) and (n<=3)):
            n -= 1
            break
        else:
            raise ValueError
    except ValueError:
        print('Error escriba un numero de distribucion de teclado samsung')

        
# Input de Datos
palabra = str(input("Ingrese la palabra a cifrar: ")).lower()
letra = list(palabra)

# Creacion de lista de cifrado segun posicion
for i in range(len(letra)):
    lista.append(cqf.Funciones.cifrado_posicional(letra[i]))

# Eliminacion de datos de tipo NoneType
while True:
    if None in lista:
        lista.remove(None)
    else:
        break

# Input de la tabla a usar para cifrar
salto = int(input('Ahora diga el salto para cifrarlo usando el metodo de cifrado qwerty: ')) - 1

# Impresion del mensaje cifrado
lista_cesar = cqf.Funciones.cifrado_qwerty(salto + 1, lista)
print(f'El cifrado cesar de la palabra {palabra} con un salto de {salto+1} es:', end=' ')
for i in lista_cesar:
    print(i, end='')