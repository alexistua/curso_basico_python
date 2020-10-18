#Ejemplo si queremos imprimir en pantalla numeros del 1 al 1000.

#si no usaramos ningun bucle, tendriamos que hacerlo como el siguiente ejemplo
#hasta llegar a 1000.

print(1)
print(2)
print(3)
print(4)
print(5)

#Si resolvemos este problema con el ciclo while, el codigo seria el siguiente

contador = 1 #definimos la variable que va ir aumentado
print(contador) #imprimimos el contador
while contador < 1000: #miestras el contador sea < a 1K, ejecuta el codigo de abajo
    contador += 1 # Esto es lo mismo que contador = contador + 1 (es un atajo)
    print(contador)

# si queremos resolver con el ciclo for lo que hicimos con el ciclo while,
#hacemos lo siguiente:

for contador in range(1000): #para el contador en el rango que va del 0 al 1000,
    print(contador)          #la variable contador en el ciclo va ir tomando los
                             #valores del rango, al principio desde 0 hasta
                             #llegar al 999.

#En el ejemplo anterior le estamo diciendo a python que haga un ciclo que va ir
#desde el 0 hasta el numero antes que tenemos en el rango, es decir 999.

#para poder imprimir desde el 1 al 1000, como en el ciclo while, podemos pasarle
#a la funcion range dos parametros, primero el valor inicial desde el que
#queremos partir y por ultimo el valor final, pero toma en cuenta que el valor
#final siempre llega hasta una posicion anterior al rango, Ejemplo:

for contador in range(1, 1001): #para el contador en el rango que va del 1 al 1001
    print(contador)             #vamos a imprimir el valor del contador en cada
                                #vuelta del ciclo (1 al 1000).

#tambien podemos convertir este rango(tipo de datos) en una lista, ejemplo:

a = list(range(1, 1001))
print(a)

#Ultimo ejemplo: Imprimir la tabla del 11

for i in range (10): #para la variable i, en el rango que va del 0 al 9
    print(11 * i)    #vamos a imprimir en cada vuelta del ciclo 11 por el valor
                     #de la variable i.
