#is vs == y mutabilidad
###Mision:  Haz ejemplos con números grandes, strings y listas para ver cuándo is es True o False.

#Analiza si los valores son equivalentes (Si los valores son iguales)
a = 1000
b = 1000
print(a == b) #Retorna True
print(a is b) #Retorna True

#Analiza si los valores son iguales (si ocupan el mismo espacio de memoria)
a = [1,2,3]
b = [1,2,3]
print(a == b) #Retorna True
print(a is b) #Retorna False