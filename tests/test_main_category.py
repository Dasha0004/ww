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


if __name__ == "__main__":
    unittest.main()
