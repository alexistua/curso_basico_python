dolares = input ('cuantos dolares tienes?:')
dolares = float (dolares)
cambio = input ('Cual es el cambio de del dia?:')
bolivares = dolares * cambio
bolivares = round (bolivares, 2)
bolivares = str (bolivares)
print ('Tienes Bs. ' + bolivares + ' bolivares')
