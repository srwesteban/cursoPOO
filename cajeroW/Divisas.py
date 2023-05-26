class Divisas:
    Dolar, Euro, Yen, Libra = 4650, 4980, 785, 5050

    def conversion(self, tipo, monto):
        conversiones = {1: self.Dolar, 2: self.Euro, 3: self.Yen, 4: self.Libra}
        return monto * conversiones.get(tipo, 1)

    def divi(self):
        print('tipo de moneda\n1. Dolar\n2. Euro\n3. Yen\n4. Libra\n5. COP\n')
