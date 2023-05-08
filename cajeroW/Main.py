from Banco import Banco
from Cajero import Cajero
from Usuarios import Usuario

if __name__ == '__main__':

    banco = Banco()
    banco.menu()
    BD = banco.seleccionar_banco()
    cuenta = input("Ingresa tu numero de cuenta ")
    contrasena = input("Ingresa tu contraseña: ")
    usuario = Usuario(cuenta, contrasena)
    nombre = usuario.validar_banco(BD)
    numero = usuario.enviar_usuario(nombre)
    cajero = Cajero()
    usuario.validar_usuario(nombre)
    cajero.limpiar_pantalla()

    print('Bienvenid@ ' + nombre + '\n')

    while True:

        cajero.menu()
        opcion = abs(int(input('Ingrese una opción: ')))
        cajero.limpiar_pantalla()
        if opcion == 1:
            print('Su saldo es: ')
            cajero.consultar(numero)
        elif opcion == 2:
            cantidad = abs(int(input('ingrese la cantidad: ')))
            print('Su nuevo saldo es: ')
            cajero.consignar(cantidad, numero)
            cajero.actualizar()
        elif opcion == 3:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a depositar: ')))
            cantidad = cajero.conversion(tipo, monto)
            print('Su nuevo saldo es: ')
            cajero.consignar(cantidad, numero)
            cajero.actualizar()
        elif opcion == 4:
            cantidad = abs(float(input('Ingrese la cantidad a retirar: ')))
            print(cajero.retirar(cantidad, numero))
            print(f"Su nuevo saldo es: ")
            cajero.consultar(numero)
            cajero.actualizar()
        elif opcion == 5:
            cajero.divi()
            tipo = abs(int(input('ingrese el tipo de moneda: ')))
            monto = abs(float(input('Ingrese la cantidad a retirar: ')))
            cantidad = cajero.conversion(tipo, monto)
            print(cajero.retirar(cantidad, numero))
            print(f'Su nuevo saldo es:')
            cajero.consultar(numero)
            cajero.actualizar()
        else:
            print("fin del programa")
            cajero.actualizar()
            break
