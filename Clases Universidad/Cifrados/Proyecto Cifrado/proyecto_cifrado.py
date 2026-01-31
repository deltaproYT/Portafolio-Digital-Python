import cifrado_fun as cf

# Input de datos
lista = []
palabra = str(input("Ingrese la palabra a cifrar: "))
letra = list(palabra)

# Creacion de lista de conversion de letra a numero posicional
for i in range(len(letra)):
    lista.append(cf.cifrado_posicional(letra[i]))

# Proceso de eliminacion de None en la lista
while True:
    if None in lista:
        lista.remove(None)
    else:
        break

# Input de Salto
salto = int(input('Ahora diga el salto para cifrarlo usando el metodo de cifrado cesar: ')) - 1

# Conversion de cifrado posicional a texto legible usando el salto ingresado por el usuario para aplicar el cifrado Cesar
lista_cesar = cf.cifrado_cesar(salto, lista)
print(f'El cifrado cesar de la palabra {palabra} con un salto de {salto+1} es:', end=' ')
for i in lista_cesar:
    print(i, end=' ')