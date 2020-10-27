#Al igual que en la enumeracion exhaustiva y la aproximacion de soluciones vamos a buscar un valor cercano a la raiz cuadrada que digite el usuario.
def busqueda_binaria():
    objetivo = int(input('Escribe un número al cual desees obtener la raíz cuadrada: '))
    epsilon = 0.001
    bajo = 0.0                  #Definimos nuestro limite inferior.
    alto = max(1.0, objetivo)   #Utilzamos la funcion max(nos regresa el valor mas alto entre dos valores), si el objetivo es menor a 1.0, entonces empezamos directamente en 1.0
    respuesta = (alto + bajo) / 2 #inicializamos nuestra respuesta inicial y donde vamos almacenarel resultado final una vez culmine las iteraciones(ciclos).

    #vamos a generar nuestra iteracion, ver si la respuesta al cuadrado - el objetivo, se va acercando al valor que queremos encontrar (objetivo).
    #Mientras el valor absoluto se vaya acercando a epsilon (0.01), significa que cada vez vamos a llegar mas cerca.
    #No hay necesidad de colocar una segunda condicion en el ciclo, porque en con el alto nos estamos garantizando que nuestro objetivo lo minimo que va a poder ser es 1.0
    #Es decir nos aseguramos de que no vamos a tener numeros negativos.
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta #si esto se cumple, bajo es nuestra nueva respuesta.
        else:                #caso contrario, alto es nuestra nueva respuesta.
            alto = respuesta

        #En cada ciclo estamos dividiendo entre 2 nuestro espacio de busqueda y estamos redefiniendo que es bajo y que es alto y estamos modificando nuestra respuesta.
        #Cada vez que generamos nuestra respuesta adicional, vamos a irla cambiandola para saber si es nuestro limite alto o nuestro limite bajo.
        respuesta = (alto + bajo) / 2  
    
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

    #receuerda que la busqueda binaria unicamente funciona cuando nuestro conjunto tiene un orden, si no esta ordenado hay que busvar en todas las opciones.


if __name__ == "__main__":
    busqueda_binaria()