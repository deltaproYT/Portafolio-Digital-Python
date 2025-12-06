    #Print -- Imprimir en consola

# print("Hola Mundo")


     #Tipos de datos
    #Comando Type -- Ver el tipo de dato
#print(type("Hola Mundo")) # str
#print(type(5)) # int
#print(type(5.5)) # float
#print(type(True)) # bool

     


#     #int -- Entero
# NumeroEntero = 5
#print(NumeroEntero)

     #float -- Decimal
# NumeroDecimal = 5.5
#print(NumeroDecimal)

     #str -- Cadena de texto
# Texto = "Hola Mundo"
#print(Texto)

     #bool -- Booleano (True o False)
# Booleano = True
#print(Booleano)

        #Concadenar -- Unir cadenas de texto
# Texto1 = "Hola"
# Texto2 = "Mundo"
# Texto3 = Texto1 + " " + Texto2
# print(Texto3)


        #Formato de cadenas -- Formatear cadenas de texto
# Nombre = "Juan"
# Edad = 25
# Texto = "Hola, mi nombre es {} y tengo {} años".format(Nombre, Edad)
#print(Texto)


        #Concadenar cadenas de texto con variables
# Nombre = "Juan"
# Edad = 25
# Texto = "Hola, mi nombre es " + Nombre + " y tengo " + str(Edad) + " años"
#print(Texto)


        #Asignar diferentes tipos de datos a una variable

#Nombre, Edad, Altura = "Juan", 25, 1.75
#print(Nombre, Edad, Altura)


        #Asignar el mismo valor a varias variables  

# Nombre = Edad = Altura = 25
# print(Nombre, Edad, Altura)


        #Metodos para cadenas de texto -- Funciones para cadenas de texto

#Texto = "Hola Mundo"

#print(Texto.lower()) # Convertir a minusculas

#print(Texto.upper()) # Convertir a mayusculas

#print(Texto.title()) # Convertir a mayusculas la primera letra de cada palabra

#print(Texto.strip()) # Eliminar espacios en blanco al inicio y al final

#print(Texto.replace("Hola", "Adios")) # Reemplazar una palabra por otra

#print(Texto.split(" ")) # Dividir una cadena de texto en una lista

#print(Texto.find("Mundo")) # Buscar una palabra en una cadena de texto

#print(Texto.count("o")) # Contar cuantas veces aparece una letra en una cadena de texto

#print(Texto.startswith("Hola")) # Verificar si una cadena de texto empieza con una palabra

#print(Texto.endswith("Mundo")) # Verificar si una cadena de texto termina con una palabra

#print(Texto.isalpha()) # Verificar si una cadena de texto es alfabetica   

#print(Texto.isdigit()) # Verificar si una cadena de texto es numerica

#print(Texto.isalnum()) # Verificar si una cadena de texto es alfanumerica

#print(Texto.islower()) # Verificar si una cadena de texto es minuscula

#print(Texto.isupper()) # Verificar si una cadena de texto es mayuscula

#print(Texto.isspace()) # Verificar si una cadena de texto es un espacio en blanco

#print(Texto.capitalize()) # Convertir la primera letra de una cadena de texto en mayuscula


        #Cambiar el tipo de dato de una variable -- Convertir un tipo de dato a otro
#NumeroEntero = 5
#NumeroDecimal = 5.5
#Texto = "Hola Mundo"
#Booleano = True

#NumeroEntero = str(NumeroEntero) # Convertir a string