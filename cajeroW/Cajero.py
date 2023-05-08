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
            # Escribe cada número de la lista en una línea separada
            for numero in self.numeros:
                f.write(str(numero) + "\n")
        f.close()

    def consultar(self, numero):
        return print(self.numeros[numero])

    def limpiar_pantalla(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def consignar(self, cantidad, numero):
        self.numeros[numero] += cantidad
        print(self.numeros[numero])

    # retirar
    def retirar(self, cantidad, numero):
        if self.numeros[numero] >= cantidad:
            self.numeros[numero] -= cantidad
            return 'operacion exitosa'
        elif cantidad > self.__Limite:
            return print("accion denegada la cantidad máxima de retiro es $2,500,000 COP.")
        else:
            return "No hay suficiente saldo, no se completo la operacion."

    # consulta

    def menu(self):
        print('')
        print('1. Consultar saldo')
        print('2. Consignacion')
        print('3. Consignacion en otras divisas')
        print('4. Retirar')
        print('5. Retirar con otras divisas')
        print('6. Salir')
