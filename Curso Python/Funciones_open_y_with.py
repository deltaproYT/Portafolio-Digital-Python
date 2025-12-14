file_name = 'Texto1.txt'

with open(file_name, 'w') as text:
    for _ in range(10):
        text.write(input('Escriba algo:') + '\n') 



with open(file_name, 'r') as text:
    data = text.read()
    for i in data.split('\n'):
        print(i)

    
