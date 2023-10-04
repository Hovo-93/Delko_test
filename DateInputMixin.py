import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class DateInput:
    def __init__(self):
        self.day = None
        self.month = None
        self.year = None

    def get_year(self):
        self.year = (input("Введите Год: "))
        return int(self.year)

    def get_day(self):
        self.day = int(input("Введите День: "))
        return int(self.day)

    def get_month(self):
        self.month = int(input("Введите начальный месяц (цифрой): "))
        return int(self.month)
