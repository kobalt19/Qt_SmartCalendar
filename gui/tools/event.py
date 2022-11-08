import datetime


class Event:
    def __init__(self, dt, text, _id, user_id):
        self.dt = dt
        self.text = text
        self.id = _id
        self.user_id = user_id

    def get_datetime(self):
        date_str, time_str = self.dt.split(' ')
        dt = datetime.datetime(*date_str.split('-'), *time_str.split(':'))
        return dt

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id

    def __str__(self):
        return f'{self.dt} - {self.text}'
