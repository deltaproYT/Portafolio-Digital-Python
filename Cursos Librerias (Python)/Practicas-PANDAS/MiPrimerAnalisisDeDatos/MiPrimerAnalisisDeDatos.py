import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Trabajos en Git/Proyectos Python (Git)/Practicas PANDAS/MiPrimerAnalisisDeDatos/ModalidadVirtual.csv')
#print(df['carrera'][0])
#print(df['carrera']=='Psicología')
#filtro = df['sexo'] == 'Mujer'
#df_filtrado = df[filtro]
#print(df_filtrado)

#Atributos del DataFrame
#print(df.info())
#print(df.shape)
#print(df.size)
#print(df.columns)
#print(df.index)
#print(df.dtypes)
#print(df.head(10)) 
#print(df.tail(10))

conteo = df['sexo'].value_counts()
conteo = conteo.sort_index()
conteo.plot.bar()
plt.show()
