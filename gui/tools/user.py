class User:
    def __init__(self, username, passwd, _id):
        self.username_encr = username
        self.passwd_encr = passwd
        self._id = _id

    def __hash__(self):
        return sum(map(hash, self.get_all()))

    def get_all(self):
        return self.username_encr, self.passwd_encr, self._id

    def get_id(self):
        return self._id

    def get_data(self):
        return self.username_encr, self.passwd_encr
