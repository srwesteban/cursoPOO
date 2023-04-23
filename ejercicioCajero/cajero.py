

class Cajero:

    Saldo = None
    Limite = 2500000
    Fecha = '10/04/2023'


    def __init__(self,saldo):
        self.Saldo = saldo


    def __str__(self):
        return f"saldo actual: {self.Saldo}"
    

    def transaccion(self,monto,fecha):
         
         if monto > self.Limite and fecha != self.Fecha:
              
              return "La transaccion supera el limite"
         
         elif monto > self.Limite and fecha == self.Fecha:
              
              return "La transaccion"
              
         
         elif monto > self.Saldo:
              
              return "Saldo insuficiente"
         
         else:
              self.Saldo -= monto
              return "transaccion exitosa"
         
         

miTransaccion = Cajero(5000000) # saldo total inicial
MontoTransaccion = int(input("ingrese el monto para retirar: "))
FechaTransaccion = input("ingrese fecha de retiro: ")

print(miTransaccion.transaccion(MontoTransaccion,FechaTransaccion))
print("fecha de transaccion: ", FechaTransaccion)
print(miTransaccion)

                  


