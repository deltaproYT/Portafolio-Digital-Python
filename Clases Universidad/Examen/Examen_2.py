'''
Examen Algoritmos y Fundamentos de Programación
Actividad 2: Analice el siguiente código y explique qué hace. Luego, ejecútelo y muestre el resultado:
'''

def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

print(suma_numeros(5))

#print(1 + 2 + 3 + 4 + 5)