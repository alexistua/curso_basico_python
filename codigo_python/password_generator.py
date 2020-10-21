#importamos el modulo random
import random

#creamos la funcion generar_contrasena, la cual no va a recibir parametros.
#vamos a crear 3 listas (mayusculas, minusculas y simbolos).
#Luego vamos a sumar a todas estas listas, en una lista unica llamada caracteres
#Ahora generamos una lista vacia, en donde vamos a poner caracteres aleatorios para generar nuestra contraseña, aqui vamos a guardar caracteres al azar de toda
#la lista "caracteres" que acabamos de generar.  
def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '@', '#', '$', '%', '&', '(', ')', '/']

    caracteres = mayusculas + minusculas + simbolos

    contrasena = []

    #Generamos un ciclo for, con un rango de 15 vueltas.
    #Creamos una nueva variable (caracter_random), utilizando la funcion random.choice, para elegir un caracter al azar de toda mi lista "caracteres"
    #y lo guardo dentro de la variable caracter_random.
    #luego vamos ha agregar a nuestra lista contraseña, otro caracter generado por nuestra variable caracter_random, y asi hasta culminar las 15 vueltas del ciclo.
    #Es decir durante cada ciclo se va ha agregar a esa lista vacia, un caracter al azar de mi lista "caracteres", hasta culminar las 15 vueltas. 
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    #Ahora vamos a covertir esta lista contrasena en un string, colocamos ''.join(contrasena), en el parentesis colocamos nuestra lista original
    #para unir en un string final, todos los caracteres unidos en una sola cadena.
    #finalmente hacemos un return a nuestra variable contraseña, para que en nuestra funcion run, al ejecutar la funcion generar_contrasena
    #la misma se guarde dentro de nuestra variable "contraseña" y asi podamos imprimir tu nueva contraseña es: contraseña.
    contrasena = ''.join(contrasena)
    return contrasena

#definimos la funcion princial, creamos la variable password que almacenara el contenido de la funcion que generara la contraseña de manera automatica.
#imprimimos en patalla, una cadena de caracteres mas el valor de la variable password.
def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


#Creamos el Entry point, para ejecutar la funcion main
if __name__ == '__main__':
    run()