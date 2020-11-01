def factorial(n):
    #Antes de generar el codigo, colocamos nuestro "docstrings", es decir, documentamos lo
    #queremos hacer con este codigo. En la primera linea indicamos lo que hace la funcion
    #definimos que n es un entero y que es mayor que o y regresa n!
    """Calcula el factorial de n.

    n int > 0
    returns n!
    """

    #empezamos nuestro codigo, escribiendo cual es nuestro caso base, es decir, hasta
    #donde nos vamos a ir adentro de esta iteracion, porque si no podriamos entrar
    #en un infinite loop, sin embargo pythin no permite generar un infinite loop en
    #recursividad, pero te va a generar un error porque llegaste al limite maximo de
    #recursividad. 

    print(n)
    if n == 0:      #Caso Base
        return 1    #si n es igual a 1, retornamos 1 porque factorial de 1 es 1.
    else:
        return n * factorial(n - 1) #regresamos la definicion matematica.
    #Con el codigo de arriba (lin 21), tenemos nuestra primera funcion recursiva.
    #por ejemplo si decimos que n = 3, no se ejectuta el codigo de la linea 18 y 19 sino la 21.

n = int(input('Escibe un entero del cual desees sabes un factorial: '))

print(factorial(n))

# if __name__ == "__main__":
#     factorial(n)

#si ejecutamos el codigo y decimos que n = 10, entonces estamos ejecutando la funcion factorial 10 veces