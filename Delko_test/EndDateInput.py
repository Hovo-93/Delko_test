from Delko_test.DateInputMixin import DateInput
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class EndInput(DateInput):

    def __init__(self):
        super().__init__()
        self.end_date = None

    def process(self):
        self.end_date = datetime.datetime(year=self.get_year(), month=self.get_month(), day=self.get_day())
        return self.end_date
