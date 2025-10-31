import unittest

from src.main_category import Category
from src.main_product import Product


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.total_product = 0
        self.category = Category()

    def test_add_product_increases_total_product(self):
        p = Product("TestProduct", 150, 10)
        self.category.add_product(p)
        self.assertEqual(Category.total_product, 1)

        p2 = Product("AnotherProduct", 200, 5)
        self.category.add_product(p2)
        self.assertEqual(Category.total_product, 2)

    def test_products_property_returns_correct_strings(self):
        p = Product("TestProduct", 150, 10)
        p2 = Product("AnotherProduct", 200, 5)
        self.category.add_product(p)
        self.category.add_product(p2)

        expected = [
            "TestProduct, 150 руб. Остаток: 10 шт.",
            "AnotherProduct, 200 руб. Остаток: 5 шт.",
        ]
        self.assertEqual(self.category.products, expected)

    def test_products_property_empty_list(self):
        self.assertEqual(self.category.products, [])

    def test_str_output(self):
        products = [
            Product("Товар 1", 5),
            Product("Товар 2", 10),
            Product("Товар 3", 0),
        ]
        category = Category("Категория А", products)
        expected = "Категория А, количество продуктов: 15 шт."
        self.assertEqual(str(category), expected)

    def test_str_empty_products(self):
        category = Category("Пустая категория", [])
        expected = "Пустая категория, количество продуктов: 0 шт."
        self.assertEqual(str(category), expected)


if __name__ == "__main__":
    unittest.main()
