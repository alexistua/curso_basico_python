#Con los diccionarios vamos a encerrar nuestros datos entre llaves.
#En python las llaves, sirven para definir diccionarios.
#Un diccionario es una estructura de datos de llaves y valores.
#Vamos ha acceder a los elementos a traves de las llaves, las llaves no son necesariamenete numeros que van de 0 al infinito.
#Con un diccionario, nosotros vamos a ponerle nombre a ese indice y el nombre que lleva ese indice se llama llave.
#A los valores del diccionarios, le llamaremos como tal valores.

#en el siguinete ejemplo vamos a crear 3 elementos, el primero va estar definido por una llave 1 y el contenido va hacer el numero "1"
#se separa la llave, del contenido con dos puntos ":"

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1']) #Asi podemos acceder al contenido de la llave1
    # print(mi_diccionario['llave2']) #Asi podemos acceder al contenido de la llave1
    # print(mi_diccionario['llave3']) #Asi podemos acceder al contenido de la llave1

    
    #Aqui este diccionario, va a contener como llaves, el nombre de los paises y como valores la poblacion que tiene cada uno.
    poblacion_paises = {          
       'Argentina': 44938712,
       'Brasil': 210147125,
       'Colombia': 50372424,
       'Venezuela': 28870000,
    }
    # print(poblacion_paises['Venezuela'])

    #ahora vamos ha aprender como aprender a recorrer el diccionario a partir de las llaves
    #Es decir hacer que el ciclo for haga 3 vueltas a traves de este diccionario y me devuelva en cada vuelva el valor de las llaves
    #es decir me diga, argentina, brasil, colombia y venezuela

    #Este es un metodo del diccionario que, me devuelve las llaves.
    # for pais in poblacion_paises.keys():   
    #     print(pais)

    #Este es un metodo del diccionario, que me devuelve el valor de las llaves en el diccionario.
    # for pais in poblacion_paises.values(): 
    #       print(pais)

    #Este es un metodo del diccionario, que me devuelve las llaves y valor de esas llaves en el diccionario.
    # for pais in poblacion_paises.items():    
    #     print(pais)

    #Como manejamos dos elementos es mejor que a diferencia del ejemplo anterior, hay que separalos por "," y colocar otro elemento como poblacion.
    for pais, poblacion in poblacion_paises.items():    
        print(pais + ' tiene ' + str(poblacion) + ' de Habitantes')                                     
    

if __name__ == '__main__':
    run()
