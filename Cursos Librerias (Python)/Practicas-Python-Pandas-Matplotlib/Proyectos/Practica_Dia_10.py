import pandas as pd
#Filtrado con condiciones
#Filtra filas donde edad > 25 y ciudad = "Quito".

df = pd.DataFrame({'Nombre': ['Jorge', 'Hugo', 'Paco', 'Luis'], 'Ciudad': ['Carchi', 'Guayaquil', 'Quito', 'Quito'], 'Edad': [19, 27, 24, 30]}) #Crea un DataFrame
Filtro1 = df.query('Ciudad == "Quito" and Edad > 25') #Crea un filtro con el atributo .query()
Filtro2 = df[(df['Ciudad'] == 'Quito') & (df['Edad'] > 25)] #Crea un filtro con el codigo df['']
print(Filtro1) #Imprime el Filtro1
print(Filtro2) #Imprime el Filtro2