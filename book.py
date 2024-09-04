class Book:
    def __init__(self, id: int, title: str, author: str, quantity: int, price: float):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price

    @classmethod
    def create(cls, title, author, quantity, price):
        return cls('-', title, author, quantity, price)

    def json(self):
        return dict(id=self.id,
                    title=self.title,
                    author=self.author,
                    quantity=self.quantity,
                    price=self.price)
