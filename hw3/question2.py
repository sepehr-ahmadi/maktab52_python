from datetime import date


class birthday:
    def __init__(self, birth_day):
        self.birth_day = birth_day

    def calculate_age_by_year(self):
        today = date.today()
        age_by_year = today.year - self.birth_day.year - (
                    (today.month, today.day) < (self.birth_day.month, self.birth_day.day))
        return age_by_year

    def calculate_age_by_day(self):
        today = date.today() - self.birth_day
        return today.days

    def calculate_days_to_birthday(self):

        return 365-self.calculate_age_by_day() % 365


m = birthday(date(1997, 2, 3))
print(m.calculate_age_by_year())
print(m.calculate_age_by_day())
print(m.calculate_days_to_birthday())
