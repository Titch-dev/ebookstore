class Account:
    TYPE = ('admin', 'customer')

    def __init__(self, id: int, username: str, password: str, acc_type: str, address=None):
        self.id = id
        self.username = username
        self.password = password
        self.acc_type = acc_type
        self.address = address

    @classmethod
    def create(cls, username, password, acc_type):
        return cls('-', username, password, acc_type)

    def json(self):
        return dict(id=self.id,
                    username=self.username,
                    password=self.password,
                    acc_type=self.acc_type,
                    address=self.address)
