# contador = 0
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

# contador = 1
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

# contador = 2
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

# contador = 3
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

# contador = 4
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

# contador = 5
# print('2 elevado a la ' + str(contador) + ' es igual a ' + str(2**contador))

def run():                          #definimos la funcion principal
    LIMITE = 1000000                #definimos una variable, que a lo largo del codigo no cambia, por lo tanto
                                    #definimos una constante cambiando el nombre de la variable a mayuscula
    contador = 0                    #definimos una variable contador, que empieza 0 y cambiara a lo largo del bucle
    potencia_2= 2**contador         #definimos esta variable que realiza el calculo de elevar a 2 al contador
    while potencia_2 < LIMITE:      #definimos el ciclo (mientras la potencia de 2 sea < al limite, ejecutamos lo que esta debajo)
        print('2 elevado a la ' + str(contador) + ' es igual a ' + str(potencia_2))
        contador = contador + 1   #contador vale 0+1 para evitar infinit loop
        potencia_2 = 2**contador  #definimos potencia_2 de nuevo

if __name__ == '__main__':
    run()
