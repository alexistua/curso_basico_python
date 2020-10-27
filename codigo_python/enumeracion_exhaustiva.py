#la enumeración exhaustiva es un tipo de algoritmo que tambien se le llama "adivina y verifica", es decir pruebalas todas hasta que la encuentres.
#En este algoritmo se prueban todos los espacios de posibilidades, para conseguir la aproximación a una respuesta.
#Este es uno de los algoritmos mas importantes en la ciencia de la computación y tambien uno de los mas sencillos.
#En este ejemplo vamos a tratar de determinar si un numero tiene una raiz cuadrada exacta.
def enumeracion_exhaustiva():
    objetivo = int(input('Escoge un número entero al cual desees sacar la raiz cuadrada: '))
    respuesta = 0 #Generamos una respuesta con un valor inicial de cero, para que empezemos nuestro contador.

    while respuesta**2 < objetivo: #Mientras que la respuesta al cuadrado sea menor al numero al que le queremos sacar la raiz.
        print(respuesta)
        respuesta +=1 #Aqui vamos aumentando el valor de la respuesta en 1, durante cada ciclo, es decir, 1*1, 2*2, 3*3, 4*4, 5*5, hasta llegar al objetivo encontremos la respuesta o nos demos cuenta que ese numero no tiene una raiz cuadrada exacta.
    
    if respuesta**2 == objetivo:
        print(f'La raíz cuadra de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')



if __name__ == "__main__":
    enumeracion_exhaustiva()