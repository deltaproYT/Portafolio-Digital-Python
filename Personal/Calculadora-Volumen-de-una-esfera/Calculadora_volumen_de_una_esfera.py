from math import pi

def Calcular_volumen_esfera_(radio):
    if radio < 0:
        return "el radio no puede ser negativo"
    else:
        volumen = (4/3) * pi * (radio ** 3)
        return "el volumen de la esfera es: " + str(volumen)
    


def Convertir_diametro_a_radio(diametro):
    return diametro / 2

print("Bienvenido a la calculadora de volumen de una esfera")
print("Quiere desea medir con el radio o el diametro?" )
print("1. Radio")
print("2. Diametro")
opcion = int(input("Ingrese una opcion: "))


if opcion == 1:
    print("Por favor, ingrese el radio de la esfera:")
    radio = float(input())

elif opcion == 2:
    print("Por favor, ingrese el diametro de la esfera:")
    diametro = float(input())
    radio = Convertir_diametro_a_radio(diametro)

else:
    print("Opcion no valida, por favor ingrese 1 o 2")
    exit()
resultado = Calcular_volumen_esfera_(radio)
print(resultado)