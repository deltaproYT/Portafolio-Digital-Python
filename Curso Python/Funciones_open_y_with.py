from pathlib import Path

# Use forward slashes or pathlib to avoid backslash-unicode escape issues on Windows
file_name = Path("C:/Users/Jordy/Visual Studio Code Principal/Repos/Python-Projects/Curso Python/texto1.txt")

with file_name.open('w', encoding='utf-8') as text:
    text.write('Hola Mundo\n'
               'Mi programador es Jordy Wladimir Ortiz Aquino\n'
               'Soy la primera prueba de una impresion fuera de la consola\n'
               'y creacion de archivo .txt\n'
               'Luego probaremos otros metodos e ideas nuevas')


with file_name.open('r', encoding='utf-8') as text:
    data = text.read()
    for i in data.split('\n'):
        print(i)

    
