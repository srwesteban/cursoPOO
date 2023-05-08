
class Usuario():

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
            return 0
        elif nombre == 'andrea':
            return 1
        elif nombre == 'benito':
            return 2
        elif nombre == 'carlos':
            return 3
        elif nombre == 'daniel':
            return 4
        elif nombre == 'jaime':
            return 5
        elif nombre == 'jesus':
            return 6
        elif nombre == 'juan':
            return 7
        elif nombre == 'lorena':
            return 8
        elif nombre == 'mercedes':
            return 9
        elif nombre == 'pablo':
            return 10
        elif nombre == 'pedro':
            return 11
        elif nombre == 'sandra':
            return 12
        elif nombre == 'sebastian':
            return 13
        else:
            return 14
