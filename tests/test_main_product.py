import sys
import unittest
from io import StringIO

from src.main_product import Product


class TestProductPrice(unittest.TestCase):

    def test_price_getter(self):
        p = Product("Test", "desc", 100, 5)
        self.assertEqual(p.price, 100)

    def test_price_setter_valid(self):
        p = Product("Test", "desc", 100, 5)
        p.price = 150
        self.assertEqual(p.price, 150)

    def test_price_setter_zero(self):
        p = Product("Test", "desc", 100, 5)

        captured_output = StringIO()
        sys.stdout = captured_output

        p.price = 0
        sys.stdout = sys.__stdout__

        self.assertEqual(p.price, 100)  # цена не изменилась
        self.assertIn(
            "Цена не должна быть нулевая или отрицательная", captured_output.getvalue()
        )

    def test_price_setter_negative(self):
        p = Product("Test", "desc", 100, 5)

        captured_output = StringIO()
        sys.stdout = captured_output

        p.price = -50
        sys.stdout = sys.__stdout__

        self.assertEqual(p.price, 100)  # цена не изменилась
        self.assertIn(
            "Цена не должна быть нулевая или отрицательная", captured_output.getvalue()
        )

    def test_new_product_classmethod(self):
        data = {
            "name": "NewProduct",
            "description": "desc",
            "price": 200,
            "quantity": 10,
        }
        p = Product.new_product(data)
        self.assertEqual(p.name, "NewProduct")
        self.assertEqual(p.description, "desc")
        self.assertEqual(p.price, 200)
        self.assertEqual(p.quantity, 10)


if __name__ == "__main__":
    unittest.main()
