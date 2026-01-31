alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789'
lista = []
lista_cesar = []

def cifrado_posicional(letra):
    cant = 0
    for i in alfabeto:
        cant += 1
        if letra == i:
            return cant

def cifrado_cesar(salto, lista):
    lista_cifrada = []
    for i in range(len(lista)):
        num = alfabeto[(int(lista[i]) + salto) % len(alfabeto)]
        lista_cifrada.append(num)

    return lista_cifrada

palabra = str(input("Ingrese la palabra a cifrar: "))
letra = list(palabra)

for i in range(len(letra)):
    lista.append(cifrado_posicional(letra[i]))

while True:
    if None in lista:
        lista.remove(None)
    else:
        break

print(f"El cifrado posicional de la palabra {palabra} es:", end=' ')
for i in lista:
    print(i, end=' ')

print('\n')


salto = int(input('Ahora diga el salto para cifrarlo usando el metodo de cifrado cesar: ')) - 1


lista_cesar = cifrado_cesar(salto, lista)
print(f'El cifrado cesar de la palabra {palabra} con un salto de {salto+1} es:', end=' ')
for i in lista_cesar:
    print(i, end=' ')