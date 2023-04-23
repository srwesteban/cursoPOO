import datetime

class Cajero():
   
    
    dinero = open("CAJEROCLASES/informacion.txt", "r")
    dinero_inicial = dinero.read()
    entidad = "bancolombia"
    numero_de_cuenta = ""
    transacciones = []
    
    def consultar_saldo_inicial(self):
        print (f"el saldo es de : {self.dinero_inicial} pesos.")

    def consultar_saldo(self):
        print(f"El saldo actual es: {self.dinero} pesos.")

    def retiros(self, retiro):

        if retiro > self.dinero or retiro >= 2500000:
            return "Imposible realizar el retiro"

        else:
            self.dinero -= retiro
            fecha = datetime.datetime.now()
            self.transacciones.append(
                (fecha, retiro, self.numero_de_cuenta, "retiro"))
            print(f"Retiro exitoso \n Dinero retirado: {retiro} \n Fecha: {fecha} \n Saldo actual: {self.dinero} pesos")

    def consignacion(self, deposito):

        self.dinero += deposito
        fecha = datetime.datetime.now()
        self.transacciones.append((fecha, deposito, "deposito"))
        print(f"Se ha depositado {deposito} pesos \n Fecha: {fecha} \n Saldo actual: {self.dinero} pesos")


cajero1 = Cajero()
print("Bienvenido a su cuenta")
cajero1.consultar_saldo_inicial()
cajero1.dinero = float(input("Ingrese su consignacion incial a su cuenta: "))


while True:
    print("\nPor favor seleccione una opción:")
    print("1. Consultar saldo")
    print("2. Realizar retiro")
    print("3. Realizar consignación")
    print("4. Salir")

    opcion = int(input("Ingrese el número de opción: "))

    if opcion == 1:
        cajero1.consultar_saldo()
    elif opcion == 2:
        valor_retiro = float(input("¿Cuál es la cantidad que desea retirar? "))
        cajero1.retiros(valor_retiro)
    elif opcion == 3:
        valor_deposito = float(input("Ingrese la cantidad que desea depositar: "))
        cajero1.consignacion(valor_deposito)
    elif opcion == 4:
        print("Gracias por utilizar nuestros servicios.")
        break
    else:
        print("Opción no válida. Por favor intente de nuevo.")