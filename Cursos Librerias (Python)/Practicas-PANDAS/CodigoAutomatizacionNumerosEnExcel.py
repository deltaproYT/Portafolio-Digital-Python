import random
import pandas as pd

# Parámetros
cantidad = 600
rango_min = 1000
rango_max = 9999

# Verifica que el rango sea suficiente
if cantidad > (rango_max - rango_min + 1):
    raise ValueError("La cantidad excede el número de valores únicos posibles en el rango.")

# Generar números aleatorios sin repetir
numeros = random.sample(range(rango_min, rango_max + 1), cantidad)

# Crear DataFrame
df = pd.DataFrame(numeros, columns=["Números Aleatorios"])

# Guardar en Excel
df.to_excel("numeros_aleatorios.xlsx", index=False)

print("¡Archivo Excel creado con éxito!")
