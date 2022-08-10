from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('Factory', 10)

    def test_init_paint_factory(self):
        self.assertEqual('Factory', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_property_ingredients(self):
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_ingredient_not_a_valid_product_type(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('alabala', 5)
        self.assertEqual(f"Ingredient of type alabala not allowed in {self.paint_factory.__class__.__name__}", str(context.exception))

    def test_add_a_valid_ingredient(self):
        product_type = 'white'
        quantity = 1
        result = self.paint_factory.add_ingredient(product_type, quantity)
        self.assertEqual(1, self.paint_factory.ingredients[product_type])
        self.assertIn(product_type, self.paint_factory.ingredients)
        new_quantity = 3
        result = self.paint_factory.can_add(new_quantity)
        self.assertEqual(1, self.paint_factory.ingredients[product_type])

    def test_add_new_valid_ingredient(self):
        self.paint_factory.add_ingredient('yellow', 0)
        self.assertEqual(0, self.paint_factory.ingredients['yellow'])
        self.paint_factory.ingredients['blue'] = 0
        self.assertEqual(2, len(self.paint_factory.ingredients))

    def test_raises_value_error_when_over_the_capacity(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('yellow', 20)
        self.assertEqual('Not enough space in factory', str(context.exception))

    def test_remove_not_present_ingredient_raises_exception(self):
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('alabala', 3)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_remove_correctly_when_value_over_zero(self):
        product_quantity = 3
        self.paint_factory.add_ingredient('yellow', 5)
        self.paint_factory.remove_ingredient('yellow', product_quantity)
        self.assertEqual(2, self.paint_factory.ingredients['yellow'])
        self.assertDictEqual({'yellow': 2}, self.paint_factory.ingredients)

    def test_remove_raises_error_when_product_below_zero(self):
        product_quantity = 10
        ingredient = 'blue'
        remove_quantity = 11
        self.paint_factory.add_ingredient(ingredient, product_quantity)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient(ingredient, remove_quantity)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(context.exception))

    def test_property_products(self):
        self.paint_factory.ingredients = {'yellow': 2, 'blue': 3}
        self.assertEqual(2, len(self.paint_factory.ingredients))
        self.paint_factory.ingredients['white'] = 3
        self.assertEqual(3, len(self.paint_factory.ingredients))
        self.assertDictEqual({'yellow': 2, 'blue': 3, 'white': 3}, self.paint_factory.ingredients)

    def test_products_property_returns_correct_ingredients(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 5)
        result = self.paint_factory.products
        expected = {"white": 5, "yellow": 5}
        self.assertEqual(expected, result)

    def test_represent_method_returns_correct_string(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 5)
        result = str(self.paint_factory)
        expected = f"Factory name: Test with capacity 10.\nwhite: 5\nyellow: 5\n"
        self.assertEqual(expected, result)

    def test_can_add_returns_true_if_quantity(self):
        result = self.paint_factory.can_add(5)
        self.assertEqual(True, result)

        result = self.paint_factory.can_add(10)
        self.assertEqual(True, result)

    def test_can_add_returns_false_if_not_valid_quantity(self):
        result = self.paint_factory.can_add(15)
        self.assertEqual(False, result)























if __name__ == '__main__':
    main()