import pandas as pd
import matplotlib.pyplot as plt

#Inactivar linea de abajo despues de la conversion excel --> CSV
#BaseExc = pd.read_excel('Trabajos en Git/Proyectos Python (Git)/Practicas PANDAS/Analisis de datos/Lista-de-clientes-con-nombre-y-direccion.xlsx') 
BaseCSV = pd.read_csv('Trabajos en Git/Proyectos Python (Git)/Practicas PANDAS/Analisis de datos/Lista-de-clientes-con-nombre-y-direccion.csv')

#print(BaseCSV.iloc[:5,1])
#print(BaseCSV.loc[:7,('Nombre completo','Teléfono')])
#BaseCSV['Nueva Columna'] = pd.Series(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
#print(BaseCSV)
#NuevaColumna = BaseCSV.pop('Nueva Columna')
#print(BaseCSV)
#FiltroGC = BaseCSV[(BaseCSV['Grupo de clientes'] == 'C') & (BaseCSV['Correo electrónico'].str.contains('@gmail.com', case=False))]
#OrdenGC = FiltroGC.sort_values(by='Fecha de nacimiento', ascending=True)
#print(OrdenGC.dropna())


FiltroCorreo = BaseCSV['Correo electrónico'].str.contains('gmail', case=False)
#print(BaseCSV[FiltroCorreo])
OrdenNacimiento = BaseCSV.sort_values(by='Fecha de nacimiento')
BaseCSV['Edad'] = BaseCSV['Fecha de nacimiento'].str.extract(r'(\d{4})').astype(int)
print(OrdenNacimiento[FiltroCorreo])

#conteo = BaseCSV['Grupo de clientes'].value_counts()
#conteo = conteo.sort_index()
#conteo.plot.bar()
#plt.show()