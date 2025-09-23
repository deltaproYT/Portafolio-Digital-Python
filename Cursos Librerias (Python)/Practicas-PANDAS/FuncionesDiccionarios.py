import pandas as pd

Diccionario = pd.Series({'hola' : 4 , 'Mundo' : 5 , 'me' : 2 , 'llamo' : 5 , 'Jordy' : 5  })
#print(Diccionario.sort_values())
#print(Diccionario[Diccionario == 5])
#print(Diccionario.sort_index(ascending=True))
#print(Diccionario.sort_index(ascending=False))


#data = 18

#Serie = pd.Series(data, index=[0,1,2,3,4,5,6])
#print(Serie)

data_list = ['Victor', 'Jordy', 'Yiliam']
indices = ['UTPL', 'ISTER', 'UCSG']

Universidades = pd.Series(index=indices, data=data_list)
print(Universidades)