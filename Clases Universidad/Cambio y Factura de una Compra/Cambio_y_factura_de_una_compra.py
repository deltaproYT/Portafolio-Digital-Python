import sys
from pathlib import Path
from datetime import datetime

subtotal = total = cant = 0

numero_factura = 1
file_path = Path(f"Python-Projects/Clases Universidad/Cambio y Factura de una Compra/Facturas/Factura.txt")

class Almacen:
    
    
        
    def __init__(self, objetos, precios, total_cantidades=0):
        self.file_path = file_path
        self.objetos = objetos
        self.precios = precios
        self.total_cantidades = int(total_cantidades) if isinstance(total_cantidades, (int, float)) else 0
        self.subtotal = 0.0
        self.total15 = 0.0
        self.total = 0.0

    def final_factura(self):
        self.total15 = self.subtotal * 0.15
        self.total = self.subtotal + self.total15
        with self.file_path.open('a') as factura:
            factura.write(f'''
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
                              Subtotal = {self.subtotal}
                              Total 15% = {self.total15}
                              Total = {self.total}
''')

    def mostrar_lista_de_objetos(self):
        print('Los objetos en Stock son:\n')
        for i in range(len(self.objetos)):
            print(f'{i+1}# :{self.objetos[i]} | Precio: {self.precios[i]}$')
    
    def añadir_factura(self, i, cant, total):
        with self.file_path.open('a') as factura:
            factura.write(f'                              {self.objetos[i]} ====== > Precio: {self.precios[i]}$ x Cantidad: {cant} ==== > {total} \n')
class Cliente:
    def __init__(self, nombre_cliente, numero_identificacion):
        self.nombre_cliente = nombre_cliente
        self.numero_identificacion = numero_identificacion    

class Funciones(Cliente):
    def __init__(self, nombre_cliente, numero_identificacion, numero_factura):
        self.numero_factura = numero_factura
        self.file_path = file_path
        super().__init__(nombre_cliente, numero_identificacion)
    
    
    def cabeza_factura(self):
        with self.file_path.open('w') as factura:
            factura.write(f'''                                Almacenes SINNOMBRE
                          Factura no. {self.numero_factura} -- Emitida a: {self.nombre_cliente} : {self.numero_identificacion}
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
                           \n
                           \n''')
    

    


stock = Almacen(['Lapiz','Boligrafo','Resma de Hojas','Cuaderno Academico','Mochila','Cartulina'], [0.50, 1.00, 2.00, 4.00, 25.00, 0.75], 0)



nombre_cliente = input('Por favor ingrese su nombre\n')
numero_identificacion = input('Por favor ingrese su numero de identificacion\n')
f = Funciones(nombre_cliente, numero_identificacion, numero_factura)
f.cabeza_factura()
while True:
    try:
        stock.mostrar_lista_de_objetos()
        print('Para terminar el proceso escriba "-1"')
        i = int(input('Ingrese el numero de Item: '))
        if i == -1:
            break
        cant = int(input('Ingrese la Cantidad: '))
        total = (stock.precios[i-1] * cant)
        stock.añadir_factura(i-1, cant, total)
        stock.subtotal += (stock.precios[i-1] * cant)

    except KeyboardInterrupt:
        print('\n\nSaliendo mediante teclado...')
        sys.exit()
    except ValueError:
        print('Ingrese un valor valido')
    except IndexError as e:
        print(f'Por favor ingrese un numero dentro del rango de la lista {e}')

stock.final_factura()
print('Gracias por su Compra :)')