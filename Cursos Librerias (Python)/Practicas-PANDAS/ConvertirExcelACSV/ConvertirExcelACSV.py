import pandas as pd

excdf = pd.read_excel('Trabajos en Git/Proyectos Python (Git)/Practicas PANDAS/ConvertirExcelACSV/BD_anuario_2024.xlsx')
excdf.to_csv('Trabajos en Git/Proyectos Python (Git)/Practicas PANDAS/ConvertirExcelACSV/BD_anuario_2024.csv', index=None, header=True)
