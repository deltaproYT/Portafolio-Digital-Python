import pandas as pd
import matplotlib.pyplot as plt

#Pandas + Matplotlib
#Haz un gráfico de barras de promedios por grupo.

df = pd.DataFrame({'Nombre': ['Jorge', 'Hugo', 'Paco', 'Luis'], 'Ciudad': ['Carchi', 'Guayaquil', 'Quito', 'Quito'], 'Edad': [19, 27, 24, 30]}) #Crea un DataFrame
print(df) #Imprime el DataFrame original

dffiltrado = df.groupby('Ciudad')['Edad'].mean() #Agrupa por la ciudad y saca el promedio de toda la columna edad
plt.barh(df,dffiltrado) #Crea una grafica de barras horizontales
plt.show() #imprime la grafica

