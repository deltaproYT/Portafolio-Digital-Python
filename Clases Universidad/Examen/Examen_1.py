'''
Examen Algoritmos y Fundamentos de Programación
Actividad 1: Cree un programa en Python que muestre los números del 10 al 1 en forma descendente 
utilizando while. 
'''

num = 10
num_list = []
while num > 0:
    num_list.append(num)
    #print(num)
    num -= 1

print(num_list)