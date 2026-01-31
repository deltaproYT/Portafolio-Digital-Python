class Funciones:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789'

    @staticmethod
    def cifrado_posicional(letra):
        cant = 0
        for i in Funciones.alfabeto:
            cant += 1
            if letra == i:
                return cant
            
    @staticmethod        
    def cifrado_cesar(salto, lista):
        lista_cifrada = []
        for i in range(len(lista)):
            num = Funciones.alfabeto[(int(lista[i]) + salto) % len(Funciones.alfabeto)]
            lista_cifrada.append(num)
        return lista_cifrada