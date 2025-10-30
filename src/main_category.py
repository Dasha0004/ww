class Category:
    total_categories = 0
    total_product = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        # Если products передан, используем его, иначе пустой список
        self.__products = products if products is not None else []

        Category.total_categories += 1
        Category.total_product += len(self.products)

    def add_product(self, product):
        # Метод для добавления продукта в приватный список
        self.__products.append(product)
        Category.total_product += 1

    @property
    def products(self):
        # Возвращаем список строк с описанием каждого продукта
        return [
            f"{p.name}, {p.price} руб. Остаток: {p.stock} шт." for p in self.__products
        ]
