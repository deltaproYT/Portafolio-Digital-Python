import numpy as np
#NumPy — Indexación y slicing
#Mision: Cambia toda la primera fila de una matriz a -1.
matriz = np.arange(9).reshape(3,3) #Crea Matriz 3x3 con numeros del 1-9
matriz[0,:] = -1 #Escoge la primera fila y cambia los valores por -1
print(matriz) #Imprime la matriz resultante