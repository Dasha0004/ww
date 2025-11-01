from abc import ABC, abstractmethod


class InitInfoMixin:
    def __init__(self, *args, **kwargs):
        # Вывод информации о классе и параметрах
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами args={args}, kwargs={kwargs}"
        )
        # Вызываем следующий __init__ в MRO
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = None
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self._price = value

    @abstractmethod
    def __str__(self):
        pass

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                f"Нельзя сложить объекты разных типов: {type(self).__name__} и {type(other).__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity


class Product(InitInfoMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
