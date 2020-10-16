#Cada vez que ejectute o llame la funcion conversor, voy a terner
#que decirle que tipo de pesos voy a trabajar y el valor del dolar.
#tipo_pesos y valor_dolar son parametros.
def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')

menu = '''
Bienvenidos al conversor de monedas 💰

1 - Pesos Argentinos
2 - Pesos Chilenos
3 - Pesos Colombianos
4 - Pesos Mexicanos

Elige una opcion: '''

opcion = int(input(menu))

if opcion == 1:
    conversor('Argentinos', 77.41) #se ejectuta la funcion conversor
elif opcion == 2:
    conversor('Chilenos', 798.80)
elif opcion == 3:
    conversor('Colombianos', 3839)
elif opcion == 4:
    conversor('Mexicanos', 21.36)
else:
    print('Por favor ingresa una opcion correcta: ')
