import pandas as pd
import numpy as np

#amigos = {'Nombre': ['Victor', 'Jordy', 'Yiliam'], 'Curso': ['3C','3C','3C'], 'Edad': [18,18,18],'Carrera': ['Ciberseguridad','Redes','Negocios Internacionales']}
#Serie = pd.DataFrame(amigos)
#print(Serie)

#fulvito = pd.DataFrame([['Messi','Barcelona'],['Cristiano','Real Madrid'],['Dembele','PSG']], columns= ['Jugador', 'Equipos'])
#print(fulvito)

df = pd.DataFrame(np.random.randn(4,3), columns= ['a','b','c'])
print(df)
