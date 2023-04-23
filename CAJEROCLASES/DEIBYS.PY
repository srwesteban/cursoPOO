import datetime


class CajeroElectronico:
    def __init__(self, id_cuenta, saldo_inicial):
        self.id_cuenta = id_cuenta
        self.saldo = saldo_inicial
        self.limite_diario = 2500000

    def consultar_saldo(self):
        return self.saldo

    def hacer_retiro(self, monto):
        if monto > self.limite_diario:
            return "No se puede realizar el retiro porque excede el límite diario"
        elif monto > self.saldo:
            return "No se puede realizar el retiro porque el monto es mayor que el saldo disponible"
        else:
            self.saldo -= monto
            ahora = datetime.datetime.now()
            mensaje = f"Retiro exitoso. Fecha y hora: {ahora}. Monto retirado: {monto}. Saldo disponible: {self.saldo}"
            return mensaje

    def hacer_consignacion(self, monto):
        self.saldo += monto
        ahora = datetime.datetime.now()
        mensaje = f"Consignación exitosa. Fecha y hora: {ahora}. Monto consignado: {monto}. Saldo disponible: {self.saldo}"
        return mensaje

    def hacer_transferencia(self, cuenta_destino, monto):
        if monto > self.saldo:
            return "No se puede hacer la transferencia porque el monto es mayor que el saldo disponible"
        else:
            self.saldo -= monto
            cuenta_destino.saldo += monto
            ahora = datetime.datetime.now()
            mensaje = f"Transferencia exitosa. Fecha y hora: {ahora}. Monto transferido: {monto}. Saldo disponible: {self.saldo}"
            return mensaje


id_cuenta = input("Ingrese su número de cuenta: ")
saldo_inicial = float(input("Ingrese su saldo inicial: "))

cajero = CajeroElectronico(id_cuenta, saldo_inicial)

while True:
    print("Seleccione una opción:")
    print("1. Consultar saldo")
    print("2. Hacer un retiro")
    print("3. Hacer una consignación")
    print("4. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        saldo_actual = cajero.consultar_saldo()
        print(f"Su saldo actual es: {saldo_actual}")
    elif opcion == "2":
        monto = float(input("Ingrese el monto que desea retirar: "))
        mensaje_retiro = cajero.hacer_retiro(monto)
        print(mensaje_retiro)
    elif opcion == "3":
        monto = float(input("Ingrese el monto que desea consignar: "))
        mensaje_consignacion = cajero.hacer_consignacion(monto)
        print(mensaje_consignacion)
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")

# Escribir el saldo final en un archivo de texto
with open(f"{id_cuenta}.txt", "w") as archivo:
    archivo.write(f"Número de cuenta: {id_cuenta}\n")
    archivo.write(f"Saldo disponible: {cajero.consultar_saldo()}")

