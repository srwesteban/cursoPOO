retiro = int(input("ingrese el monto a retirar: "))
saldo = 1501000


if retiro > saldo:
    print("no hay saldo suficuente")
elif retiro > 1500000:  
    print("no se puede retirar mas de 1,500,000")

else:
    saldo -= retiro
    print("saldo retirado: ", retiro )
    print("saldo disponible: ", saldo)
