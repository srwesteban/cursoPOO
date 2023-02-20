phonebook = open("ejerciciosLibro/addressbook.txt","r")
numEntries = 0
eof = False
while not eof: # mientras eof no sea falso, es decir sea verdadero termina el bucle
# asigna las variables a cada linea de texto 
    lastName = phonebook.readline().rstrip()
    firstName = phonebook.readline().rstrip()
    street = phonebook.readline().rstrip()
    citystatezip = phonebook.readline().rstrip()
    homephone = phonebook.readline().rstrip()
    mobilephone = phonebook.readline().rstrip()
    if lastName !="": # si lastname es diferente de un espacio
        #acumulador
        numEntries = numEntries + 1
    else: #eof es verdadero, acaba el ciclo
        eof = True
print("tienes", numEntries ,"entradas en tu libreta de direcciones.")