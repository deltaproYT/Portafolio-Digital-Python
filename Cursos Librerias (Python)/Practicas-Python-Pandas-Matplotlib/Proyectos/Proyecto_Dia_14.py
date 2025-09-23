import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Repositories/Practicas Python Pandas-Matplotlib/Data/Stress_Dataset.csv')
df = df.sort_values(by = 'Age')
#print(df)

#Conteo = df['Gender'].value_counts() #Hace un conteo de los grupos que hay en la columna 'gender'
#Conteo = Conteo.sort_index() #Ordena los indices
#Conteo.plot.bar() # Crea un grafico 
#plt.show()  #Conclusion 1: Mas personas del genero '0' respondieron a la encuesta que las personas del genero '1'

#Agrupacion = df.groupby('Have you recently experienced stress in your life?')['Age'] #Agrupa las edades a traves del nivel de estres que hayan acumulado en sus vidas
#y = df['Have you recently experienced stress in your life?'] #Crea el eje y de la grafica
#x = df['Age'] #Crea el eje x de la grafica


#plt.barh(x ,y) #Crea la grafica de barras en base a los dos ejes
#plt.xlabel('Age') #Asigna el nombre al eje y 'age'
#plt.ylabel('Have you recently experienced stress in your life?') #Asigna nombre al eje x
#plt.legend #Muestra los textos
#plt.show() #Conclusion 2: Los rangos mas altos de estres se encuentran en las edades de 18,19,20,21,22, 24 y 100 años

x = df['Have you noticed a rapid heartbeat or palpitations?'].value_counts().sort_index() #Recoje la informacion sobre las personas que han sentido palpitaciones durante periodos de estres
y = df['Do you struggle to find time for relaxation and leisure activities?'].value_counts().sort_index() #Recoje la informacion sobre si las personas pueden encontrar formas de camarse o relajarse

plt.plot(x.index, x.values, color='purple', label = 'Have you noticed a rapid heartbeat or palpitations?') #Crea la grafica 1
plt.plot(y.index, y.values, color='green', label = 'Do you struggle to find time for relaxation and leisure activities?') #Crea la grafica 2
plt.legend(loc = 'lower left') #Muestra el bloque de texto en la esquina inferior izquierda
plt.show() #Conclusion 3: mas pulsaciones o palpitaciones tengan las personas, mas dificil se les hace encontrar formas de relajacion o formas de calmarse (supongo que son ataques de ansiedad por estres)
