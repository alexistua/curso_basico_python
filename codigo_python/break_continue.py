def run():
#    for contador in range(1000): #para el contador del rango que va del 0 al 999, vamos a imprimir solo los numeros pares.
#        if contador % 2 != 0:    #si al contador al dividirlo por 2, el resto de la division es distinto de 0
#            continue             #te saltas la vuelta del ciclo y lo que esta debajo de la palabra continue, no se va a ejectutar
#        print(contador)          #cada vez que el ciclo se encuentra con la variable contador, siendo un numero impar nos vamos a
                                  #saltar la vuelta del ciclo y no vamos a imprimir ese contador.

#   for i in range(10000):   #para la variable "i" en el rango que vade 0 a 9999
#       print(i)             #imprimimos la variable i en cada vuelta del ciclo
#       if i ==5678:         #y si la variable i en algun momento es igual a 5678
#           break            #utilizamos la palabra break para cortar el ciclo y no seguir ejecutando

#Tip Pro:(Es un estandar nombrar "i" a la variable que va ir cambiando de valor,
#es un standar de los desarrolladores, usar "i" para el ciclo for.

    texto = input('Escribe un texto: ') #creamos una variable texto y le solicitamos al usario escribir un texto.
    for letra in texto:                 #para cada letra "en" el texto, es decir, vamos a recorrer esa cadena de catacteres y vamos a ir por cada letra
        if letra == 'o':                #si la letra de ese texto, contiene una letra 'o', cortamos el ciclo y no seguimos ejecutando.
            break                       #mientras tanto vamos a imprir a esa letra.
        print(letra)


if __name__ == '__main__':
    run()
