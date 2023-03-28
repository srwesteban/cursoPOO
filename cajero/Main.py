from Cajero import Cajero, menu


if __name__ == '__main__': # la manera de tener una clase main en python donde inicia la ejecucion
    archivo = 'saldo.txt' # el archivo que contiene saldo
    cajero = Cajero(archivo) # creacion del objeto pide un archivo por parametro

    while True: # la manera de acer un Do While en python
        menu()
        opcion = input('Ingrese una opción: ')
        if opcion == '1': # consultar
            print(f'Su saldo es: {cajero.consultar()}')
        elif opcion == '2': # consignar
            cantidad = abs(float(input('Ingrese la cantidad a depositar: ')))
            cajero.consignar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar()}')
            #retirar
        elif opcion == '3':
            cantidad = abs(float(input('Ingrese la cantidad a retirar: ')))
            print(cajero.retirar(cantidad))
            print(f"Su nuevo saldo es: {cajero.consultar()}")
        else:
            print("fin del programa")
            break;