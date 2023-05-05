

from Cajero import Cajero


class Usuario(Cajero):

    def __init__(self, cuenta, contrasena):
        self.Cuenta = cuenta
        self.Contrasena = contrasena

    def validar(self,bd):
        try:
            with open(bd, 'r') as archivo:
                for linea in archivo:
                    usuario, contrasena_archivo, nombre = linea.strip().split(',')
                    if usuario == self.Cuenta and contrasena_archivo == self.Contrasena:
                        return nombre
        except FileNotFoundError:

            return None

    def enviarUsuario(self, nombre):
        if nombre == 'ana':
            return 'data_users/ana.txt'
        elif nombre == 'andrea':
            return 'data_users/andrea.txt'
        elif nombre == 'benito':
            return 'data_users/benito.txt'
        elif nombre == 'carlos':
            return 'data_users/carlos.txt'
        elif nombre == 'daniel':
            return 'data_users/daniel.txt'
        elif nombre == 'jaime':
            return 'data_users/jaime.txt'
        elif nombre == 'jesus':
            return 'data_users/jesus.txt'
        elif nombre == 'juan':
            return 'data_users/juan.txt'
        elif nombre == 'lorena':
            return 'data_users/lorena.txt'
        elif nombre == 'mercedes':
            return 'data_users/mercedes.txt'
        elif nombre == 'pablo':
            return 'data_users/pablo.txt'
        elif nombre == 'pedro':
            return 'data_users/pedro.txt'
        elif nombre == 'sandra':
            return 'data_users/sandra.txt'
        elif nombre == 'sebastian':
            return 'data_users/sebastian.txt'
        else:
            return 'data_users/william.txt'
