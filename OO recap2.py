class Data:
    def __init__(self, dzien, miesiac, rok):
        self.__dzien = dzien
        self.__miesiac = miesiac
        self.__rok = rok

    def __str__(self):
        return f'Jest dzien {self.__dzien} i rok {self.__rok}'

    def zmien_date(self, dzien, miesiac, rok):
        print('walidacja')
        self.__dzien = dzien
        self.__miesiac = miesiac
        self.__rok = rok

moja_data = Data(12, 12, 2022)
print(moja_data)