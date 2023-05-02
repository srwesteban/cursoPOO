
from Divisas import Divisas


class Cajero(Divisas):
    __Limite = 2500000  # variable privada
    
    archivo = 'Bancolombia.txt'

    def __init__(self, archivo):

        with open(archivo, 'r') as saldo:
            self.saldo = float(saldo.read())

    def limpiarPantalla(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def consignar(self, cantidad):
        self.saldo += cantidad
        with open(self.archivo, 'w') as f:
            f.write(str(self.saldo))  # escribe el archivo saldo

    # retirar

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            with open(self.archivo, 'w') as f:
                f.write(str(self.saldo))
                return 'operacion exitosa'
        elif cantidad > self.__Limite:
            return print("accion denegada la cantidad máxima de retiro es $2,500,000.")
        else:
            return "No hay suficiente saldo."

    # consulta

    def consultar(self):
        with open(self.archivo, 'r') as f:
            return float(f.read())

    def menu(self):
        print('1. Consultar saldo')
        print('2. Consignacion')
        print('3. Consignacion en otras divisas')
        print('4. Retirar')
        print('5. Retirar con otras divisas')
        print('6. Salir')
