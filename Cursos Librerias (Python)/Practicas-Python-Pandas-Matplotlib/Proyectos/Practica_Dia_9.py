import pandas as pd
#Selección con .loc y .iloc
#Selecciona la segunda fila y tercera columna.

df = pd.DataFrame({'Hombres': ['Juan', 'Luis', 'Enrique'], 'Mujeres': ['Juana', 'Luisa', 'Enriqueta'], 'Animales': ['Junio', 'Lulu', 'elton']}) #Crea un DataFrame
print(df) #Imprime el DataFrame
print(df.loc[1,'Animales']) #Utiliza el comando loc para ubicar un elemento mediante el uso de nombres
print(df.iloc[1,2]) #Utiliza el comando iloc para ubicar un elemento mediante la posicion