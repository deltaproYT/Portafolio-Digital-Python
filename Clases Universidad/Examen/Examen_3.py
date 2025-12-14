'''
Examen de Algoritmos y Fundamentos de Programación
Actividad 3: Hacer un codigo que cumpla los siguientes requisitos 
• Defina una función calcular_factorial(n) 
• Use un ciclo for para calcular el factorial 
• Solicite el número al usuario y muestre el resultado 
'''
import sys
def calcular_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact
while True:
    try:
        num = int(input('Por favor, ingrese un numero entero: '))
        if num <= 0:
            raise ValueError
        break
    except ValueError as e:
        print(f'Por favor ingrese un valor valido Error:({e})') 
    except KeyboardInterrupt:
        print('Gracias por usar el programa. Cierre Forzado')
        sys.exit()


print(calcular_factorial(num))