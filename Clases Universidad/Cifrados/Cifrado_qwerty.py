qwerty = ('qwertyuiopasdfghjklñzxcvbnm', f'''1234567890@#$_&-+()/*"':;!?''', '~`|•√π÷×§∆£¢€¥^°={{}}\%©®™✓[]'.format())
lista = []
lista_cesar = []
n = 0
def cifrado_posicional(letra):
    cant = 0
    global n
    for i in qwerty[n]:
        cant += 1
        if letra == i:
            cant -= 1
            return cant

def cifrado_qwerty(salto, lista):
    lista_cifrada = []
    num_list = salto % 3 
    

    for i in range(len(lista)):
        num = qwerty[num_list][int(lista[i])]
        lista_cifrada.append(num)

    return lista_cifrada
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
    
palabra = str(input("Ingrese la palabra a cifrar: ")).lower()
letra = list(palabra)

for i in range(len(letra)):
    lista.append(cifrado_posicional(letra[i]))

while True:
    if None in lista:
        lista.remove(None)
    else:
        break

print('\n')


salto = int(input('Ahora diga el salto para cifrarlo usando el metodo de cifrado qwerty: ')) - 1


lista_cesar = cifrado_qwerty(salto + 1, lista)
print(f'El cifrado cesar de la palabra {palabra} con un salto de {salto+1} es:', end=' ')
for i in lista_cesar:
    print(i, end='')