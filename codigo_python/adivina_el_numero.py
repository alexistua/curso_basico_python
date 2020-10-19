# para este ejercicio utilizaremos un modulo de Python, que es un paquete de
#codigo, que tenemos disponible para ejecutar funciones, que hacen el trabajo
#por nosotros, para este ejercicio, utilizaremos el modulo random para trabajar
#con las alatoriedades del lenguaje.

import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Escribe un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))    
    print('Ganaste!!!')


if __name__ == '__main__':
    run()
