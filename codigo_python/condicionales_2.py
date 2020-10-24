def main():
    
    # entero_1 = int(input('Escribe un número entero :'))
    # entero_2 = int(input('Escribe otro entero: '))
    
    
    # if entero_1 > entero_2:
    #     print('El primer número es mayor que el segundo.')
    # elif entero_1 < entero_2:
    #     print('El segundo número es mayor que el primero.')
    # else:
    #     print('Los dos números son iguales.')  

    deudor = input('Escribe el nombre del Deudor: ')
    co_deudor = input('Escribe el nombre del Co-Deudor: ')
    edad1 = int(input('Escribe la edad del Deudor: '))
    edad2 = int(input('Escribe la edad del Co-Deudor: '))


    if edad1 > edad2:
        print(f'La edad de {deudor} es mayor a la de {co_deudor}.')
    elif edad1 < edad2:
        print(f'La edad de {co_deudor} es mayor que la de {deudor}.')
    else:
        print('Ambos edad1es tienen la misma edad.')


if __name__ == "__main__":
    main()
    