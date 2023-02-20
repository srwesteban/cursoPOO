# Escribir un programa que almacene en una lista n números y los muestre por pantalla de menor a mayor.

cantidad =int(input("cuantos numeros desea ingresar\n"))
lista = []
i=0
while i < cantidad:
    numero = int(input("ingrese un numero: "))
    lista.append(numero)
    i += 1
lista.sort()
print(lista)