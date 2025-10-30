class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = None  # Инициализация приватного атрибута
        self.price = price  # Через сеттер с проверкой
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self._price = value
