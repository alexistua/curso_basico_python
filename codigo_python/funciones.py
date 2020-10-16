#def imprimir_mensaje():
#    print('Mensaje Especial')
#    print('Estoy aprendiendo a usar funciones!')

#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

# def conversacion(mensaje):
#     print('Hola')
#     print('Como estas?')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('Elige una opcion (1, 2, 3): '))
# if opcion ==  1:
#     conversacion('Elegiste la opcion 1')
# elif opcion == 2:
#     conversacion('Elegiste la opcion 2')
# elif opcion == 3:
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Por favo elige una opcion correcta')

def suma(a, b):                   #defino la funcion
    print('Se suman dos numeros') #imprimimos en pantalla esta cadena de texto
    resultado = a + b             #se crea la variable resulado, que suma 2 num
    return resultado              #se devuelve la sumatoria de 1+4, es decir, 5
                                  #ese 5 se almacena en la variable sumatoria.
sumatoria = suma(1, 4)
print(sumatoria)
