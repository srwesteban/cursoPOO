from Banco import Banco
from Cajero import Cajero

if __name__ == '__main__':

    banco = Banco()
    archivo = ''

    print('seleccione su banco')
    banco.menu()

    opcion = abs(int(input('Ingrese una opción: ')))
    if opcion == 1:
        archivo = banco.Davivienda
    elif opcion == 2:
        archivo = banco.BBVA
    elif opcion == 3:
        archivo = banco.Colptaria
    elif opcion == 4:
        archivo = banco.Citybank
    else:
        pass

    cajero = Cajero(archivo)

    cajero.limpiarPantalla()

    while True:

        cajero.menu()
        opcion = abs(int(input('Ingrese una opción: ')))
        cajero.limpiarPantalla()
        if opcion == 1:  # consultar
            print(f'Su saldo es: {cajero.consultar()}')

        elif opcion == 2:
            cantidad = abs(int(input('ingrese la cantidad: ')))
            cajero.consignar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar()}')

        elif opcion == 3:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a depositar: ')))
            cantidad = cajero.conversion(tipo, monto)
            cajero.consignar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar()}')

        elif opcion == 4:
            cantidad = abs(float(input('Ingrese la cantidad a retirar: ')))
            print(cajero.retirar(cantidad))
            print(f"Su nuevo saldo es: {cajero.consultar()}")

        elif opcion == 5:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a retirar: ')))
            cantidad = cajero.conversion(tipo, monto)
            cajero.retirar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar()}')

        else:
            print("fin del programa")
            break
