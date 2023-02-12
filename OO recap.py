class Audi:
    def __init__(self, kolor, info_o_kondycji, vin):
        self.kolor = kolor
        self.przebieg = 10
        self.kondycja = info_o_kondycji
        self.vin = vin

    def pokaz_vin(self):
        print(self.__vin)

    def aktualizuj_przebieg(self, o_ile):
        self.przebieg += o_ile

    def zmien_vin(self, nowy_vin):
        self.__vin = nowy_vin


moje_auto = Audi('czerwony', 'dobra', 'RTC2231')
print(moje_auto.kolor)

