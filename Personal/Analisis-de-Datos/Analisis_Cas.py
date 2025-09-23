import matplotlib.pyplot as plt
import pandas as pd

#Analisis de Datos
##Carga el archivo Excel y muestra las primeras 5 filas.

df = pd.read_csv('Trabajos en Git/Proyectos Python (Git)/Personal/Analisis de Datos/Datos G.csv')
#print(df.head(5))

##- ¿Cuántos estudiantes hay en total?
#print(df.shape[0])

##¿Cuáles son los nombres de las columnas?
#print(df.columns)

##¿Qué tipo de datos tiene cada columna?
#print(df.info())

##- Filtra los estudiantes que tienen menos de 20 años.
#FiltroA = df[df['Edad'] < 20]
#print(FiltroA)

##Selecciona solo las columnas de “Edad” y “Puntaje Autoestima”
#ndf = df['Edad']
#mdf = df['Puntaje Autoestima']
#ndf = pd.concat([ndf,mdf], axis = 1)
#print(ndf)

##¿Cuántos estudiantes tienen puntaje de ansiedad mayor a 80?
#FiltroB = df[df['Puntaje Ansiedad'] > 80]
#print(FiltroB.shape[0])

##¿Cuál es el promedio de autoestima para estudiantes mayores de 25 años?
#FiltroC = df.query('Edad > 25')
#print(FiltroC['Puntaje Autoestima'].mean())

##Agrupa por “Sexo” y calcula el promedio de ansiedad.
#print(df.groupby('Sexo')['Puntaje Autoestima'].mean())

##¿Qué sexo tiene mayor puntaje promedio de autoestima?
#print(df.groupby('Sexo')['Puntaje Autoestima'].mean().idxmax())

##- Agrupa por edad y muestra el conteo de estudiantes por edad.
#print(df.groupby('Edad').size())
#print(df.groupby('Edad').value_counts().sort_index())


##¿Cuál es la desviación estándar del puntaje de ansiedad?
#print(df['Puntaje Ansiedad'].std())

##- Crea un histograma del puntaje de ansiedad
#plt.hist(df['Puntaje Ansiedad'], bins=200, color='skyblue', edgecolor='black')
#plt.title('Distribución de Ansiedad')
#plt.xlabel('Puntaje')
#plt.ylabel('Número de estudiantes')
#plt.show()

##- Haz un gráfico de dispersión entre ansiedad y autoestima
#plt.scatter(df['Puntaje Ansiedad'],df['Puntaje Autoestima'])
#plt.xlabel('Puntaje Ansiedad')
#plt.ylabel('Puntaje Autoestima')
#plt.show()

##- Crea un gráfico de barras comparando el promedio de autoestima por sexo
#FiltroD = df.groupby('Sexo')['Puntaje Autoestima'].mean().reset_index()
#FiltroD.columns = ['Sexo', 'Promedio']
#plt.bar(FiltroD['Sexo'], FiltroD['Promedio'])
#plt.xlabel('Sexo')
#plt.ylabel('Promedio Autoestima')
#plt.show()

## ¿Puedes visualizar la distribución de edades con un gráfico adecuado?
#std = df['Edad'].value_counts().sort_index()
#plt.pie(std, labels=std.index, autopct='%1.1f%%')
#plt.show()

##Encuentra los 10 estudiantes con mayor ansiedad y grafícalos.
#FiltroE = df.nlargest(10, 'Puntaje Ansiedad')
#print(FiltroE)

##¿Qué correlación hay entre ansiedad y autoestima?
plt.hist(df['Puntaje Ansiedad'], bins=100, color='skyblue', edgecolor='black')
plt.title('Distribución de Ansiedad')
plt.xlabel('Puntaje Ansiedad')
plt.ylabel('Número de estudiantes')
plt.show()