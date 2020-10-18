#primero recuerda las buenas practicas, y define la funcion principal (run) y
#vamos a definir un entry point.

#Con este ejem. vamos ha aprender a recorrer una cadena de caracteres (strings)
#es decir, vamos a tomar la cadena de caracteres y vamos a generar un ciclo
# que vaya caracter por caracter desde el principio hasta el final.

def run():
#    nombre = input('Escribe tu nombre: ')
#    for letra in nombre:                 #para las letras en el nombre
#        print(letra)                     #vamos a imprimir cada letra, en cada
                                          #vuelta del ciclo. letra es la variable
                                          #que va a representar acada uno de los
                                          #caracteres en cada una de las
                                          #repeticiones de nuestro ciclo for.

#Ejemplo 2: Vamos a pedirle al usuario que escriba una frase, y luego  vamos a
#tomar cada uno de los caracteres de esta frase y vamos a imprimirlos en cosola
#en cada vuelta del cliclo en mayuscula.

     frase = input('Escribe una Frase: ')
     for caracter in frase:
         print(caracter.upper())


if __name__ == '__main__':
    run()
