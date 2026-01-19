import json
from pathlib import Path
from datetime import datetime
'''
Un JSON (JavaScript Object Notation) es un formato ligero y legible por humanos 
para el intercambio de datos, utilizado principalmente para la comunicación 
entre servidores y aplicaciones web

El modulo JSON permite leer y convertir datos de python a json y viceversa
'''

#Funciones
#json.dump(diccionario, archivo abierto)
#Permite guardar un diccionario y convertirlo en un JSON
Persona_JSON = {
    'Nombre': 'Jordy', 
    'Apellido': 'Ortiz', 
    'Mayor_de_Edad': True, 
    'Año_de_Nacimiento': 2007
    }


with open(Path('C:/Users/Jordy/Visual Studio Code Principal/Repos/Python-Projects/Cursos Librerias (Python)/Practicas JSON/JSON/persona_json.json'), 'w') as file:
    json.dump(Persona_JSON, file)

#json.load()
#Permite cargar JSON en formato .json convertirlos a diccionarios python
with open('C:/Users/Jordy/Visual Studio Code Principal/Repos/Python-Projects/Cursos Librerias (Python)/Practicas JSON/JSON/persona_json.json', 'r') as file:
    Persona_JSON_archivo = json.load(file)

    for i in Persona_JSON_archivo:
        print(f'{i} : {Persona_JSON_archivo[i]}')
    print('\n\n')

#json.loads()
#Permite cargar JSON en formato string y convertirlo a diccionario python

persona_json_string = json.loads('{"Nombre": "Jordy", "Apellido": "Ortiz", "Mayor_de_Edad": true, "A\u00f1o_de_Nacimiento": 2007}')

for i in persona_json_string:
    print(f'{i} : {persona_json_string[i]}')


#JSON serializer
'''
Hay tipos de datos no compatibles con JSON como los datetime o time
para esos escenarios se realiza un serializador o serializer, en esta
parte de la guia se expondra como hacer un serializador para datos tipo datetime
'''

fechas_json = {
    'fecha1' : datetime(2007, 6, 10),
    'fecha2' : datetime(2007, 7, 2),
    'fecha3' : datetime(2025, 2, 18),
    'fecha4' : datetime.now()
}

with open(Path('C:/Users/Jordy/Visual Studio Code Principal/Repos/Python-Projects/Cursos Librerias (Python)/Practicas JSON/JSON/fechas_json.json'), 'w') as file:
    json.dump(fechas_json, file, default=lambda x : x.isoformat())