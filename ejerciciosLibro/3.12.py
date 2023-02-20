s = input("Ingrese numeros enteros con espacios:")
lst = s.split() # la lista de enteros ahora es una lista de cadenas
count = 0 # aumulador
for e in lst:
    count += 1 #contador
print("Aqui hay", count ,"elementos en la lista.")