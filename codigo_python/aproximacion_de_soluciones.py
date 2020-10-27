#Algoritmo de Aproximacion de soluciones:
#Este algoritmo es silimilar a enumeracion exhaustiva pero no necesita una respuesta exacta.
#Con este algoritmo podemos aproximarnos a la respuesta, con un marge de error que llamaremos "epsilon".
#Epsilon vendria siendo la diferencia entre la realidad y la aproximacion.
#Mientras mas nos acerquemos a la solucion, es decir, miestras epsilon sea mas preciso (mas pequeño), la computadora ejecutara mas ciclos de computo para llegar a esta solucion.
#Ahora si queremos aproximarnos tan exacta a la respuesta, la computadora ira mas rapido, es decir, ejectura menos ciclos para aproximarnos al objetivo.
#Dicho lo anterior, para este tipo de algoritmos no podemnos tener las dos cosas, ser mas precisos y ser mas rapido.
#En el siguiente ejemplo vamos a buscar la raiz cudrada de un número, aunque sea aproximada, es decir, cuando la raiz no es exacta. 
def aproximacion():
    objetivo = int(input('Escribe un numero al cual desees obtener la raíz cuadrada: '))
    epsilon = 0.01      #Este es nuestro factor de aproximacion, que tancerca queremos llegar a la respuesta.
    paso = epsilon**2   #Definimos que tanto nos vamos a ir acercandonos en cada iteracion (en cada ciclo) a la respuesta.
    respuesta = 0.0     #vamos a inicializar donde vamos a guardar nuestra respuesta y empezamos en 0.0, es decir, guarda el resultado una vez culmine las iteraciones.

    #Creamos el loop, utilizando la funcion abs(nos regresa el valor absoluto)
    #vamos a ver si la respuesta**2 - objetivo, se va acercando al valor que queremos encontrar (objetivo).
    #Mientras el valor absoluto se vaya acercando a epsilon (0.01), significa que cada vez vamos a llegar mas cerca.
    #Para eliminar problemas con numeros negativos que ocasionarian un infinite loop, respuesta**2 - objetivo, tiene que ser menor o igual al objetivo.
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta) #Para la ver lo que sucede en cada ciclo, ejecutamos un print Statement para ver la expresion.
        respuesta += paso   #En cada iteracion se sumamos el paso a la respuesta, es decir, le vamos aumentar en cada ciclo el paso,
                            #nuestra respuesta inicia en 0.01 y en cada iteracion(ciclo) le estamos subiendo el epsilon al cuadrado, hasta acercarnos a la respuesta.

    if abs(respuesta**2 - objetivo) >= epsilon:                #si el valor absoluto de la respuest al cudrado menos el objetivo, es mayor o igual a epsilon.
        print(f'No se encontro la raíz cudrada de {objetivo}') #si no llegamos a la solucion, mostramos al usuario en pantalla que no se encontro la respuesta.
    else:                                                      #De lo contrario, se encontro la respuesta y se muestra al usuario en pantalla.
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == "__main__":
    aproximacion()