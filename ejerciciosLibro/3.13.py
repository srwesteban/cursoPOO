
r = "ejerciciosLibro/" # ruta donde se va a guardar en mi pc
filename = input("Ingrese un nombre para el archivo: ") # nobre del archivo
yourName = input("Cual es tu nombre? ")
age = int(input("Cual es tu edad? "))
outfile = open(r+filename ,"w") # creacion de archivo
outfile.write("Hola "+ yourName +". como estas?\n")
outfile.write("El proximo cumple tu edad sera: "+ str(age+1) \
+"\n")
outfile.close()# cerrar y guardar archivo