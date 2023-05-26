class Banco:
    Davivienda, Bancolombia, Citybank, BBVA, Colptaria = "bd/Davivienda.txt", "bd/Bancolombia.txt", "bd/Citybank.txt", "bd/BBVA.txt", "bd/Colpatria.txt"
    def seleccionar_banco(self):
        opciones = {1: self.Davivienda, 2: self.BBVA, 3: self.Colptaria, 4: self.Citybank}
        opcion = abs(int(input('Ingrese una opción: ')))
        return opciones.get(opcion, self.Bancolombia)
    def menu(self):
        print('Seleccione su banco:\n1.Davivienda\n2.BBVA\n3.Colpatria\n4.Citybank\n5.Bancolombia\n')


