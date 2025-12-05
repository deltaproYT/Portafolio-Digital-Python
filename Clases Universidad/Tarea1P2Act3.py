'''
Pide al usuario ingresar 10 números. 
El algoritmo debe contar cuántos son positivos, cuántos negativos y cuántos son 
ceros, y mostrar los resultados al final. 
Puede utilizar cualquiera de los ciclos revisados en clases 
'''
pos = neg = zer = int()
i = 0

while True:
    try:
        num = float(input((f'Por favor ingrese un numero {i + 1}/10:')))
        if num < 0: 
            neg += 1
            i += 1
        if num > 0:
            pos += 1
            i += 1
        if num == 0:
            zer += 1
            i += 1
        if i == 10:
            break
    except ValueError:
        print('Por favor ingrese un valor valido')

print(f'Habian:\n{pos} numeros positivos\n{zer} ceros\n{neg} numeros negativos')