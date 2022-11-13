import datetime


class Event:
    def __init__(self, dt, text, _id, user_id):
        self.dt = dt
        self.text = text
        self.id = _id
        self.user_id = user_id
        self.first = False
        self.second = False

    def __eq__(self, other):
        return self.get_data() == other.get_data()

    def get_datetime(self):
        date_str, time_str = self.dt.split(' ')
        return datetime.datetime(*map(int, date_str.split('-')), *map(int, time_str.split(':')))

    def get_first(self):
        return self.first

    def set_first(self):
        self.first = True

    def get_second(self):
        return self.second

    def set_second(self):
        self.second = True

    def notified(self):
        return self.first and self.second

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def get_data(self):
        return self.dt, self.text, self.id, self.user_id

    def get_user_id(self):
        return self.user_id

    def __str__(self):
        return f'{self.dt} - {self.text}'
