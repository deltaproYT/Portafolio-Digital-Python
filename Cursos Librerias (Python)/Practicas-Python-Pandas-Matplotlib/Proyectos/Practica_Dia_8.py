import pandas as pd
#Crear y explorar DataFrames
#Crea un DataFrame desde un diccionario y usa .info() y .describe().

df = pd.DataFrame({'Numeros Pares': [2,4,6,8,10], 'Numeros Impares': [1,3,5,7,9]}) #Creo un DataFrame
#print(df)
df.info() #Imprime la informacion sobre el dataframe
print(df.describe()) #imprime la informacion estadistica del dataframe
