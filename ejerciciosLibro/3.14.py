phonebook = open("ejerciciosLibro/addressbook.txt","r")
numEntries = 0
# asigna a lastname la primera linea del registro
lastName = phonebook.readline().rstrip()
while lastName !="":
#Dado que el string lastname no esta vacío lee el resto del registo
# asigna las siguientes lineas del registro
    firstName = phonebook.readline().rstrip()
    street = phonebook.readline().rstrip()
    citystatezip = phonebook.readline().rstrip()
    homephone = phonebook.readline().rstrip()
    mobilephone = phonebook.readline().rstrip()
    # acumulador
    numEntries += 1
    # asigna a lastname la siguiente linea del registro
    lastName = phonebook.readline().rstrip()
print("tienes", numEntries ,"entradas en tu libreta de direcciones.")