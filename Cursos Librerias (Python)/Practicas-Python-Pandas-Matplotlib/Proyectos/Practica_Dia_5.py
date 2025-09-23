import numpy as np
#NumPy — Broadcasting
#Mision: Suma un vector [1,2,3] a todas las filas de una matriz 3x3.
matriz = np.zeros((3,3)) #Crea una matriz 3x3 de 0s
vector = [1,2,3] #Crea un vector a partir de una lista
matriz = matriz + vector #Llena todas las posiciones de filas y columnas con los valores del array
print(matriz) #Imprime la matriz
