def es_primo(numero):               #Le metemos a la funcion es_primo el parametro numero
    contador = 0

    for i in range(1, numero + 1):  #para i en el rango de 1 al numero, sumamos 1 mas porque el rango llega hasta el numero anterior.
        if i == 1 or i == numero:   #para cada vuelta del ciclo, Si se cumple cualquiera de las 2 condiciones, por ejm. i= 17 y numero= 17,
            continue                #ejecutas continue para saltar el ciclo y no ejecutar la operacion, porque es primo.
        if numero % i == 0:         #Si no nos saltamos la vuelta al contador(ciclo) al dividir el numero entre i, si hay un resto, es decir
            contador += 1           #si el resultado del resto de la divion es igual a 0, tuvimos un divion exacta y no es un numero primo, sumamos 1 al contador
    if contador == 0:               #salimos del ciclo y preguntamos, si el contador es igual a 0, si al numero al dividirlo por todos los numeros que estan entre
        return True                 #1 y si mismo, dieron todas las diviones inexactas, es decir nunca tuvimos un resto igual 0 por lo cual
    else:                           #el contador nunca aumento retornamos verdadero, el numero es primo.
        return False


def run():
    numero =  int(input('Escribe un numero: '))
    if es_primo(numero):                           #Esto es lo mismo que decir, if es_primo(numero) == true, pero como el resultado de la funcion
        print('Es primo')                          #es igual a True, podemos obviar preguntar si algo es igual a verdadero. Python entiende que lo
    else:                                          #que nosotros estamos preguntando, es si el resultado de esta funcion es igual a True, ejecuta
        print('No es primo')                       #esto sino ejecuta este otro.



if __name__ == __main__:
    run()
