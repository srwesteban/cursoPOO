class Cajero:

    __Limite = 2500000 # variable privada

    def __init__(self, archivo):
        self.archivo = archivo
        try:
            with open(archivo, 'r') as saldo:
                self.saldo = float(saldo.read())
        except FileNotFoundError: # si no encuentra el archivo lo crea
            with open(archivo, 'w') as saldo:
                saldo.write('0')
            self.saldo = 0

# consignar

    def consignar(self, cantidad):
        self.saldo += cantidad
        with open(self.archivo, 'w') as f:
            f.write(str(self.saldo)) # escribe el archivo saldo
# retirar

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            with open(self.archivo, 'w') as f:
                f.write(str(self.saldo))
        elif cantidad > self.__Limite:
            return print("accion denegada la cantidad máxima de retiro es $2,500,000.")
        else:
            return print("No hay suficiente saldo.")

# consulta

    def consultar(self):
        with open(self.archivo, 'r') as f:
            return float(f.read())

def menu(): # menu
    print('1. Consultar saldo')
    print('2. Depositar')
    print('3. Retirar')
    print('4. Salir')
