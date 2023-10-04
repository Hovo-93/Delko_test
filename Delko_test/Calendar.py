from datetime import datetime, timedelta
from StartDayInput import StartInput
from EndDateInput import EndInput


class Calendar:
    def __init__(self, start_input, end_input):
        self.start_input = start_input
        self.end_input = end_input
        self.start_date = None
        self.end_date = None
        self.current_date = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_date is None:
            self.start_date = self.start_input.process()
            self.end_date = self.end_input.process()
            self.current_date = self.start_date

        while self.current_date <= self.end_date:
            formatted_date = self.current_date.strftime("%-d %B")
            self.current_date += timedelta(days=1)
            return formatted_date
        raise StopIteration


class Iterator:
    def __iter__(self):
        return Calendar(start_input, end_input)


start_input = StartInput()
end_input = EndInput()
calendar = Iterator()
for day in calendar:
    print(day)
