#Ej. 1, imprimimos numeros del 100 al 5000, multiplicando por 10 has ta cumplir el ciclo.
#Ej. 2, usamos el ejemplo 1, pero cortamos el ciclo si contador es igual a 1000

def run():
#    contador = 10
#    print(contador)
#    while contador < 5000:
#        contador *= 10
#        if contador == 1000:
#            break
#        print(contador)

#Ej. 3, Escriba un programa que pida dos números enteros,El programa pedirá de
#nuevo el segundo número mientras no sea mayor que el primero. El programa
#escribiendo los dos números.

#    print('Numero Mayor')
#    numero = int(input('Escriba un numero: '))
#    numero2 = int(input('Escriba un numero mayor que ' + str(numero) + ': '))

#    while numero2 <= numero:
#        numero2 = int(input(str(numero2) + ' no es mayor que: ' + str(numero) + ' Intentalo de Nuevo: '))

#    print()
#    print('Los numeros que has escrito son ' + str(numero) +' y ' + str(numero2))

# Ej. 4, usar continue en un ciclo while

    contador = 10
    print(contador)
    while contador < 3800:
        contador += 250
        if contador == 2760:
            continue
        print(contador)

if __name__ == '__main__':
    run()
