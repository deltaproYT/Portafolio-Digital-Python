from pathlib import Path


file_name = Path("C:/Users/Jordy/Visual Studio Code Principal/Repos/Python-Projects/Curso Python/programa1.py")

with file_name.open('w', encoding='utf-8') as text:
    text.write('print("Hello World")\nlista = []\nfor i in range(10):\n  lista.append(i)\nprint(lista)')


with file_name.open('r', encoding='utf-8') as text:
    data = text.read()
    for i in data.split('\n'):
        print(i)