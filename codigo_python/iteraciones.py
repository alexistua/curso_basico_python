def main():

#Ejemplo del ciclo while(mientras que)    
    # contador = 0
    # while contador < 10:
    #     print(contador)
    #     contador += 1     #Esto es lo mismo que contador = contador + 1

#Ejemplo de un loop dentro de otro loop (iteraciones dentro de iteraciones)
    contador_externo = 0
    contador_interno = 0

    while contador_externo < 5:
        while contador_interno < 6:
            print(contador_externo, contador_interno)
            contador_interno += 1

            if contador_interno >= 3: #Cada vez que el contador interno llegue hacer igual a 3 nos salimos de loop interno, el externo sigue corriendo.
                break
    
        contador_externo += 1 #salimos del loop e incrementamos en 1 al contador
        contador_interno = 0 #Tengo que resetear el contador interno para que corra el externo
    

if __name__ == "__main__":
    main()