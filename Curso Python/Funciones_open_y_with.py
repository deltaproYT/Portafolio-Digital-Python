file_name = 'Texto1.txt'

text = open(file_name, 'w')
for _ in range(10):
    text.write(input('Escriba algo:') + '\n') 
text.close()


text = open(file_name, 'r')
data = text.read()
for i in data.split('\n'):
    print(i)

    
text.close()