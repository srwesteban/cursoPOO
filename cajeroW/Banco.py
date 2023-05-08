class Banco:
    Davivienda = "bd/Davivienda.txt"
    Bancolombia = "bd/Bancolombia.txt"
    Citybank = "bd/Citybank.txt"
    BBVA = 'bd/BBVA.txt'
    Colptaria = 'bd/Colpatria.txt'

    def seleccionar_banco(self):
        opcion = abs(int(input('Ingrese una opción: ')))
        if opcion == 1:
            return self.Davivienda
        elif opcion == 2:
            return self.BBVA
        elif opcion == 3:
            return self.Colptaria
        elif opcion == 4:
            return self.Citybank
        else:
            return self.Bancolombia

    def menu(self):
        print('Seleccione su banco:\n')
        print('1.Davivienda')
        print('2.BBVA')
        print('3.Colpatria')
        print('4.Citybank')
        print('5.Bancolombia\n')
