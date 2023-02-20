lista=[]
cantidad = int(input("ingresa la cantidad de numeros: "))
i=1
while i<=cantidad:  

    lista.append(int(input("ingresa un numero: ")))
    i+=1

print("numero mayor: ", max(lista))    

