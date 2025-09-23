#Referencias y copias en Python
#Mision: Crea una lista, asígnala a otra variable, modifícala y comprueba si cambian juntas o no.

#Ambas variables ocupan el mismo espacio de memoria
x = [True ,1 ,'hola',4 , 45-7 ]
y = x
y.append(2) 
y.pop(0) 
print(x) #No cambia ambas variables estan conectadas al mismo espacio de memoria

#Ambas variables ocupan diferentes espacios de memoria
x = list([True ,1 ,'hola',4 , 45-7 ])
y = x
y.append(2) 
y.pop(0) 
print(x) #Variable 'x' esta anclada a una cadena y variable 'y' esta anclada a otra