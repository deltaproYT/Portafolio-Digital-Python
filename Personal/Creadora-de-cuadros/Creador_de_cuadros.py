print("Bienvenido al Creador de Cuadros")
print("Este programa te permite crear cuadros personalizados con diferentes simbolos y tamaños.")
print("primero ingrese el numero de filas que desea para su cuadro:")
filas = int(input())
print("Ahora ingrese el numero de columnas que desea para su cuadro:")
columnas = int(input())
print("Ahora ingrese el simbolo que desea usar para su cuadro:")
simbolo = input()


for i in range(filas):
    for j in range(columnas):
        print(simbolo, end="")
    print()  # Nueva línea al final de cada fila