# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

print("Ingrese las 5 notas del alumno:\n")

notas = []
suma = 0
for i in range(5):
    
    nota =(float(input(f"ingrese la nota {i+1}(entre 0 y 10)")))
    if nota < 0 or nota > 10:
        print(f"nota {nota} no es valida")
        break;
    else:
        suma += nota
        notas.append(nota)
        i+=1
        
print(f"notas: {notas}")
print(f"promedio: {suma/5}")
print(f"nota más alta: {max(notas)}")
print(f"nota menor: {min(notas)}")

