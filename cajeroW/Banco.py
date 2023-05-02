from Cajero import Cajero


class Banco:
    Davivienda = "bd/Davivienda.txt"
    Bancolombia = "bd/Bancolombia.txt"
    Citybank = "bd/Citybank.txt"
    BBVA = 'bd/BBVA.txt'
    Colptaria = 'bd/Colpatria.txt'

    def __init__(self):
        pass





    def validar(numero):
        with open('datos_bancarios.txt', 'r') as archivo:
            for linea in archivo:
                if linea.startswith(numero):
                    return True
        return False

    def menu(self):
        print('1.Davivienda')
        print('2.BBVA')
        print('3.Colpatria')
        print('4.Citybank')
        print('5.Bancolombia')







