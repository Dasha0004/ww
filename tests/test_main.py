import unittest

from src.main_category import Category
from src.main_product import Product


class TestProductCategory(unittest.TestCase):

    def test_product_initialization(self):
        p = Product("Laptop", "Powerful gaming laptop", 1500.0, 10)
        self.assertEqual(p.name, "Laptop")
        self.assertEqual(p.description, "Powerful gaming laptop")
        self.assertEqual(p.price, 1500.0)
        self.assertEqual(p.quantity, 10)

    def test_category_initialization(self):
        products = [
            Product("Laptop", "Powerful gaming laptop", 1500.0, 10),
            Product("Mouse", "Wireless Mouse", 20.0, 50),
        ]
        c = Category("Electronics", "Electronic devices", products)
        self.assertEqual(c.name, "Electronics")
        self.assertEqual(c.description, "Electronic devices")
        self.assertEqual(len(c.products), 2)

    def test_total_counts(self):
        # Сбросим счетчики, чтобы тесты не влияли друг на друга
        Category.total_categories = 0
        Category.total_product = 0

        c1 = Category(
            "Books",
            "Reading materials",
            [
                Product("Book1", "Fiction book", 12.5, 100),
                Product("Book2", "Science book", 15.0, 75),
            ],
        )
        c2 = Category(
            "Stationery", "Office supplies", [Product("Pen", "Blue pen", 1.0, 500)]
        )

        self.assertEqual(Category.total_categories, 2)
        self.assertEqual(Category.total_product, 3)


if __name__ == "__main__":
    unittest.main()
