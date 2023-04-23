class Divisas:
    Dolar = 4650
    Euro = 4980
    Yen = 785
    Libra = 5050

    def __init__(self):
        pass

    def conversion(self, tipo, monto):
        if tipo == 1:
            monto *= self.Dolar
            return monto
        elif tipo == 2:
            monto *= self.Euro
            return monto
        elif tipo == 3:
            monto *= self.Yen
            return monto
        elif tipo == 4:
            monto *= self.Libra
            return monto
        else:
            return monto

    def divi(self):
        print('tipo de moneda')
        print('1. Dolar')
        print('2. Euro')
        print('3. Yen')
        print('4. Libra')
        print('5. COP')
