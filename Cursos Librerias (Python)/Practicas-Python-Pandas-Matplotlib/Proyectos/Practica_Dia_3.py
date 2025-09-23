import numpy as np
#NumPy — Creación de arrays
#Mision: Genera una matriz 3x3 con np.arange y reshape.

Vector = np.arange(9) #Crea un vector con numeros del 1-9
matrix = Vector.reshape(3, 3) #Convierte el vector 1D en matriz 2D
print(matrix) #Imprime la matriz