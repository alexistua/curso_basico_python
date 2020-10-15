menu = '''
Bienvenidos al conversor de monedas 💰

1 - Pesos Argentinos
2 - Pesos Chilenos
3 - Pesos Colombianos
4 - Pesos Mexicanos

Elige una opcion: '''

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuantos pesos Argentinos tienes?:')
    pesos = float(pesos)
    valor_dolar = 77.41
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 2:
    pesos = input('Cuantos pesos Chilenos tienes?:')
    pesos = float(pesos)
    valor_dolar = 798.80
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 3:
    pesos = input('Cuantos pesos colombianos tienes?:')
    pesos = float(pesos)
    valor_dolar = 3839
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
elif opcion == 4:
    pesos = input('Cuantos pesos Mexicanos tienes?:')
    pesos = float(pesos)
    valor_dolar = 21.36
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')
else:
    print('Por favor ingresa una opcion correcta: ')
