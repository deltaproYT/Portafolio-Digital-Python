import sys
'''
Ejercicio 3 – Contador de vocales
Solicita una cadena de texto al usuario y cuenta cuántas vocales contiene
(ignorar si son mayúsculas o minúsculas).
'''
try:
    text = str(input('Ingrese su palabra para contar las vocales\n'))
except KeyboardInterrupt:
    print('\nSystem shutting down...') 
    sys.exit()
silaba = 0
for i in text.lower():
    if i in 'aeiou':
        silaba += 1

print(silaba)