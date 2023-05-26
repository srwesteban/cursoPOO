from Divisas import Divisas


class Cajero(Divisas):
    __Limite = 2500000  # variable privada
    numeros = []

    def __init__(self):
        super().__init__()
        self.archivo = 'data_users/usuarios.txt'
        with open(self.archivo, "r") as f:
            self.lineas = f.readlines()
            for linea in self.lineas:
                numero = float(linea)
                self.numeros.append(numero)

    def actualizar(self):
        with open(self.archivo, "w") as f:
            for numero in self.numeros:
                f.write(str(numero) + "\n")
        f.close()

    def consultar(self, numero):
        return print(self.numeros[numero])

    def limpiar_pantalla(self):
        print('\n' * 20)

    def consignar(self, cantidad, numero):
        self.numeros[numero] += cantidad
        print(self.numeros[numero])

    # retirar
    def retirar(self, cantidad, numero):
        if self.numeros[numero] >= cantidad:
            self.numeros[numero] -= cantidad
            return 'operacion exitosa'
        if cantidad > self.__Limite:
            return print("accion denegada la cantidad máxima de retiro es $2,500,000 COP.")
        else:
            return "No hay suficiente saldo, no se completo la operacion."

    def menu(self):
        print('\n'.join(['', '1. Consultar saldo', '2. Consignacion', '3. Consignacion en otras divisas', '4. Retirar', '5. Retirar con otras divisas', '6. Salir']))

