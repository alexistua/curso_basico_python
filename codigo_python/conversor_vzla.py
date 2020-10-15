bolivares = input('Cuantos bolivares tienes?:')
bolivares = float(bolivares)
cambio = input('Cual es el cambio del dia?:')
cambio = float(cambio)
dolares = bolivares / cambio
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dólares')