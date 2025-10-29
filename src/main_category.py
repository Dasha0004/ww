class Category:
    total_categories = 0
    total_product = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        # Если products передан, используем его, иначе пустой список
        self.products = products if products is not None else []

        Category.total_categories += 1
        Category.total_product += len(self.products)
