class Category:
    total_categories = 0
    total_product = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.total_categories += 1
        Category.total_product += sum(p.stock for p in self.__products)

    def add_product(self, product):
        from src.main_product import Product

        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты товаров (Product или его наследники)"
            )
        self.__products.append(product)
        Category.total_product += getattr(product, 'stock', 0)  # безопасно добавляем stock

    @property
    def products(self):
        return [
            f"{p.name}, {p.price} руб. Остаток: {p.stock} шт." for p in self.__products
        ]

    def __str__(self):
        total_quantity = sum(p.stock for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
