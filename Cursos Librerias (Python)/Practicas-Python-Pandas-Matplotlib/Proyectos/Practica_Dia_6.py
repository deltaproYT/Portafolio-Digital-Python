import matplotlib.pyplot as plt
import numpy as np
#Matplotlib — Gráficos básicos
#Dibuja una función lineal y una cuadrática en el mismo gráfico.
x = np.linspace(-10, 10, 50) #Crea una tabla de valores de -10 hasta 10 con un paso de 0.5
y1= pow(x,2) #define la operacion de x al cuadrado
y2 = x + 50 #define la funcon de x + 50

plt.plot(x,y1, label = 'Grafica F(x) = x*x') #Crea la grafica de x al cuadrado
plt.plot (x,y2, label = 'Grafica F(x) = x + 50') #Crea la grafica de x + 50
plt.legend() #Crea el cuadro de texto con titulo
plt.show() #Imprime la grafica
