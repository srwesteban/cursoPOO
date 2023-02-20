# Escribir un programa que ingrese 10 números en una lista, y los organice en la lista de menor a mayor, y escribir en pantalla los números organizados de menor a mayor.

lista = []
print("Por favor ingrese 10 numeros en la lista\n")
for i in range(10):
    lista.append(int(input(f"Ingrese un número {i+1} : ")))
lista.sort()
print(lista)