# CREACIÓN DE LA CLASE CAJERO
class cajero():
    global reg
    reg=open('CAJEROCLASES/cajeroSaldos.txt','r').readline().split(",")
    def __init__(self):
        pass
    def consultaSaldo():
        print ("Saldo: $", reg[1]) 
    def consignacion(monto,transac):
        if (transac=='R' and monto>0) or (transac=='C' and monto<0) or (monto==0) or (monto>2500000): 
            print("Valor inválido")
        else:
            reg[1] = int(reg[1])+int(monto)   
            print("Consignación exitosa. Su saldo actual es: $",reg[1])
            data=open('CAJEROCLASES/cajeroSaldos.txt','r+')
            data.seek(0)
            cta=reg[0];sld=reg[1]
            rcr=str(cta)+","+str(sld)
            data.write(str(rcr))
            data.truncate()
            data.close()
        
#INICIO ALGORITMO DE CAJERO
salir="true"
cajero1=cajero()
while (salir):
    opcCajero = input(" 1. Consulta saldo \n 2. Retiro \n 3. Consignación \n 9. Terminar \n Digite el número de la transacción que desea realizar: " )
    cajero1=cajero
    if opcCajero == "1":
        cajero1.consultaSaldo()
    elif opcCajero == "2":
        cajero1.consignacion(int(input("Monto a retirar: $"))*-1,'R')
    elif opcCajero =="3":
        cajero1.consignacion(int(input("Monto a depositar: $")),'C')
    elif opcCajero=="9":
        salir=False
    else:
        print("Opcion invalida") 