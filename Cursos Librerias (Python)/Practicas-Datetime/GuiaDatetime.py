from datetime import datetime, timedelta

##Conseguir fecha actual
## .now() - .today() - .date()
#ahora = datetime.now()  #La funcion .now() realiza la misma accion que
#hoy = datetime.today()  #la funcion .today()
#print(ahora)
#print(hoy)

#jdate = datetime.now().date() #En caso de solo necesitar solo la fecha se puede hacer uso dela funcion .date()
#print(jdate) 

##Introducir fecha personalizada
#fecha_str = '2025-02-18 15:30:15'                               #Introducimos la fecha en formato string
#fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')   #Definimos el formato de la fecha 
                                                                #Fecha: 
                                                                # %Y = Año
                                                                # %m = mes
                                                                # %d = dia
                                                                #
                                                                #Hora:
                                                                # %H = Hora
                                                                # %M = Minuto                                                #
                                                                # %S = Segundo                                                      #
#print(fecha_obj)

##Solicitud de datos de fechas
'''
Para la Solicitud de datos se podrian usar los atributos de sus respectivos datos
Fecha:
    .year - Año
    .month - Mes
    .day - Dia

Hora:
    .hour - Hora
    .minute - Minuto
    .second - Segundo
'''
#fecha_obj = datetime.strptime('2025-02-18 15:30:15', '%Y-%m-%d %H:%M:%S')
#print(fecha_obj)
#print(fecha_obj.year)
#print(fecha_obj.month)
#print(fecha_obj.day)
#print(fecha_obj.hour)
#print(fecha_obj.minute)
#print(fecha_obj.second)


##Impresion personalizada de fechas
#fecha_obj = datetime.strptime('2025-02-18 15:30:15', '%Y-%m-%d %H:%M:%S')
#fecha_format= fecha_obj.strftime('%d de %m del %Y a las %H:%M')
#print(fecha_format)

#Suma de Fechas
'''
Para realizar la suma de fechas necesitaremos una funcion especifica del modulo datetime
siendo esta la funcion timedelta

La funcion timedelta solo tiene acceso a sumar
days=n - n dias
seconds=n - n segundos
microseconds=n - n microsegundos
milliseconds=n - n milisegundos
minutes=n - n minutos
hours=n - n horas
weeks=n - n semanas
'''

#actualidad = datetime.now().date()
#print(actualidad)
#mañana = actualidad + timedelta(days=1)
#print(mañana)
#ayer = actualidad - timedelta(days=1)
#print(ayer)
#siguiente_semana = actualidad + timedelta(weeks=1)
#print(siguiente_semana)


##Tambien pueden hacerse operaciones entre fechas
#diferencia = mañana - actualidad
#print(diferencia)
#diferencia = siguiente_semana - actualidad
#print(diferencia)

#Ordenar por fecha
'''Para ordenar por fecha usaremos una building function de python llamada sorted()'''
#fechas = [
#    datetime(2026, 7, 2).date(),
#    datetime(2026, 6, 10).date(),
#    datetime(2026, 2, 18).date()
#]

#sorted(fechas, reverse=True)

#for i,j in enumerate(fechas):
#    print(f'{i+1} - {j}')
#print('\n')