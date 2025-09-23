import matplotlib.pyplot as plt
import numpy as np
#Matplotlib — Personalización
#Grafica seno y coseno con colores, títulos y leyenda personalizada.

x = np.linspace(-10, 10, 50) #Crea una tabla de valores desde -10 hasta 10 con salto de 0.5
y1 = np.sin(x) #Crea la funcion seno de x
y2 = np.cos(x) #Crea la funcion coseno de x

plt.plot(x,y1, label = 'Funcion Seno', color = 'steelblue', linewidth = 1) #Crea la grafica de la funcion seno con color azul plata
plt.plot(x,y2, label = 'Funcion Coseno', color = 'orange', linewidth = 1) #Crea la grafica de la funcion coseno con color naranja
plt.legend(loc = 'upper right') #Crea el cuadro de texto de titulo y lo ubica en la esquina superior derecha
plt.show() #imprime la grafica