import pandas as pd
#Ordenar y resetear índice
#Ordena un DataFrame por edad descendente y resetea el índice.

df = pd.DataFrame({'Nombre': ['Jorge', 'Hugo', 'Paco', 'Luis'], 'Ciudad': ['Carchi', 'Guayaquil', 'Quito', 'Quito'], 'Edad': [19, 27, 24, 30]}) #Crea un DataFrame
print(df) #Imprime el DataFrame original
df = df.sort_values(by = 'Edad', ascending=False) #Ordena los valores de manera descendente
print(df) #Imprime el DataFrame Ordenado de manera descendente
df = df.sort_values(by = 'Edad', ascending = True) #Ordena los valores de manera ascendente
print(df) #Imprime el DataFrame Ordenado de manera ascendente