import pandas as pd
#Agrupaciones con groupby
#Agrupa por ciudad y calcula edad promedio.

df = pd.DataFrame({'Nombre': ['Jorge', 'Hugo', 'Paco', 'Luis'], 'Ciudad': ['Carchi', 'Guayaquil', 'Quito', 'Quito'], 'Edad': [19, 27, 24, 30]}) #Crea un DataFrame
print(df) #Imprime el DataFrame original

df = df.groupby('Ciudad')['Edad'].mean() #Agrupa por la ciudad y saca el promedio de toda la columna edad
print(df) #Imprime el resultado