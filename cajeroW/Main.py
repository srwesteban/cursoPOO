import sys

from Banco import Banco
from Cajero import Cajero
from Usuarios import Usuario

if __name__ == '__main__':

    banco = Banco()

    print('seleccione su banco')
    banco.menu()

    BD = banco.seleccionarBanco()

    cuenta = input("Ingresa tu numero de cuenta ")
    contrasena = input("Ingresa tu contraseña: ")

    usuario = Usuario(cuenta, contrasena)
    nombre = usuario.validar(BD)

    numero = usuario.enviarUsuario(nombre)

    cajero = Cajero(numero)

    if nombre is None:
        sys.exit('Datos incorrectos fin del programa')
    else:
        pass

    cajero.limpiarPantalla()

    print('Bienvenid@ ' + nombre + '\n')

    while True:

        cajero.menu()
        opcion = abs(int(input('Ingrese una opción: ')))
        cajero.limpiarPantalla()
        if opcion == 1:  # consultar
            print(f'Su saldo es: {cajero.consultar(numero)}')

        elif opcion == 2:
            cantidad = abs(int(input('ingrese la cantidad: ')))
            cajero.consignar(cantidad,numero)
            print(f'Su nuevo saldo es: {cajero.consultar(numero)}')

        elif opcion == 3:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a depositar: ')))
            cantidad = cajero.conversion(tipo, monto)
            cajero.consignar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar(numero)}')

        elif opcion == 4:
            cantidad = abs(float(input('Ingrese la cantidad a retirar: ')))
            print(cajero.retirar(cantidad))
            print(f"Su nuevo saldo es: {cajero.consultar(numero)}")

        elif opcion == 5:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a retirar: ')))
            cantidad = cajero.conversion(tipo, monto)
            cajero.retirar(cantidad)
            print(f'Su nuevo saldo es: {cajero.consultar(numero)}')

        else:
            print("fin del programa")
            break
