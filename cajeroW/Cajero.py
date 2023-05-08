from Banco import Banco
from Divisas import Divisas


class Cajero(Divisas):

    __Limite = 2500000  # variable privada
    saldo = None

    def __init__(self, numero):
        super().__init__()

        self.archivo = 'data_users/usuarios.txt'
        with open(self.archivo, "r") as archivo:
            self.contenido = archivo.readlines()

    def limpiarPantalla(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def consignar(self, cantidad,numero):
        self.saldo += cantidad
        self.contenido[numero] = 'hola'
        return print(self.contenido[numero])



    # retirar

    def retirar(self, cantidad,numero):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            with open(self.archivo[numero], 'w') as f:
                f.write(str(self.saldo))
                return 'operacion exitosa'
        elif cantidad > self.__Limite:
            return print("accion denegada la cantidad máxima de retiro es $2,500,000.")
        else:
            return "No hay suficiente saldo."
    # consulta

    def consultar(self,numero):
         return print(self.contenido[numero])

    def menu(self):
        print('1. Consultar saldo')
        print('2. Consignacion')
        print('3. Consignacion en otras divisas')
        print('4. Retirar')
        print('5. Retirar con otras divisas')
        print('6. Salir')
