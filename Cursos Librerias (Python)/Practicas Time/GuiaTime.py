import time

##Esperar tiempo
##time.sleep(n) -> n = cantidad de segundos

#print('Hola Mundo!')
#time.sleep(10)
#print('Adios Mundo!')

##Obtener tiempo entre procesos
## time.time() - time.perf_counter()
''' Tanto la funcion time() y perf_count() hace lo mismo que es
    dar el tiempo transcurrido pero la diferencia raidca en que
    perf_counter() da ek tiempo exacto en milisegundos mientras 
    que time() solo en segundos'''

#inicio_s = time.time()
#inicio_m = time.perf_counter()
#print(f'proceso comenzado en {inicio_s} o {inicio_m}')

#time.sleep(3)

#fin_s = time.time()
#fin_m = time.perf_counter()
#print(f'proceso terminado en {fin_s} o {fin_m}')

#print(f'La diferencia de tiempo es {fin_m - inicio_m} o {fin_s - inicio_s}')