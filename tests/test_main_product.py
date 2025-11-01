import sys
import unittest
from io import StringIO

from src.main_product import LawnGrass, Product, Smartphone


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

    def setUp(self):
        self.smartphone1 = Smartphone(
            name="Phone A",
            description="A good phone",
            price=100,
            quantity=2,
            efficiency=0.9,
            model="A1",
            memory=64,
            color="Black",
        )
        self.smartphone2 = Smartphone(
            name="Phone B",
            description="Another phone",
            price=150,
            quantity=1,
            efficiency=0.85,
            model="B1",
            memory=128,
            color="White",
        )
        self.lawn_grass1 = LawnGrass(
            name="Grass A",
            description="Green grass",
            price=50,
            quantity=5,
            country="CountryX",
            germination_period=30,
            color="Green",
        )
        self.lawn_grass2 = LawnGrass(
            name="Grass B",
            description="Better grass",
            price=60,
            quantity=3,
            country="CountryY",
            germination_period=25,
            color="Dark Green",
        )

    def test_add_same_class_smartphone(self):
        result = self.smartphone1 + self.smartphone2
        expected = (self.smartphone1.price * self.smartphone1.quantity) + (
            self.smartphone2.price * self.smartphone2.quantity
        )
        self.assertEqual(result, expected)

    def test_add_same_class_lawngrass(self):
        result = self.lawn_grass1 + self.lawn_grass2
        expected = (self.lawn_grass1.price * self.lawn_grass1.quantity) + (
            self.lawn_grass2.price * self.lawn_grass2.quantity
        )
        self.assertEqual(result, expected)

    def test_add_different_classes(self):
        with self.assertRaises(TypeError):
            _ = self.smartphone1 + self.lawn_grass1

    def test_add_product_with_non_product(self):
        class Dummy:
            pass

        dummy = Dummy()
        with self.assertRaises(TypeError):
            _ = self.smartphone1 + dummy


if __name__ == "__main__":
    unittest.main()
