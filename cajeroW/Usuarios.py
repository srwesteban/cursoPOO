import sys


class Usuario:

    def __init__(self, cuenta, contrasena):
        self.Cuenta, self.Contrasena = cuenta, contrasena

    def validar_banco(self, bd):
        try:
            with open(bd, 'r') as archivo:
                for linea in archivo:
                    usuario, contrasena_archivo, nombre = linea.strip().split(',')
                    if usuario == self.Cuenta and contrasena_archivo == self.Contrasena:
                        return nombre
        except FileNotFoundError:
            return None

    def validar_usuario(self, nombre):
        if nombre is None:
            sys.exit('Datos incorrectos fin del programa')

    def enviar_usuario(self, nombre):
        nombres = ['ana', 'andrea', 'benito', 'carlos', 'daniel', 'jaime', 'jesus', 'juan', 'lorena', 'mercedes','pablo', 'pedro', 'sandra', 'sebastian']
        return nombres.index(nombre) if nombre in nombres else 14
