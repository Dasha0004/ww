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

    def test_str_output(self):
        product = Product("Товар А", "Описание", 100.99, 5)
        expected_str = "Товар А, 100 руб. Остаток: 5 шт."
        self.assertEqual(str(product), expected_str)

    def test_add_product_prices(self):
        a = Product("Товар А", "Описание А", 100, 10)
        b = Product("Товар Б", "Описание Б", 200, 2)
        self.assertEqual(a + b, 100 * 10 + 200 * 2)  # 1400

    def test_add_with_non_product(self):
        a = Product("Товар А", "Описание А", 100, 10)
        self.assertEqual(a.__add__(5), NotImplemented)

    def test_add_commutativity(self):
        a = Product("Товар А", "Описание А", 50, 4)
        b = Product("Товар Б", "Описание Б", 30, 6)
        self.assertEqual(a + b, b + a)


if __name__ == "__main__":
    unittest.main()
