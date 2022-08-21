from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('Test', 10)

    def test_init_paint_factory(self):
        self.assertEqual('Test', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertDictEqual({}, self.paint_factory.ingredients)

    def test_can_add_returns_correct(self):
        result = self.paint_factory.can_add(5)
        self.assertEqual(True, result)

        result = self.paint_factory.can_add(10)
        self.assertEqual(True, result)

    def test_can_add_over_capacity(self):
        result = self.paint_factory.can_add(15)
        self.assertEqual(False, result)

    def test_invalid_ingredient_raises_ex(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient('Purple', 5)
        self.assertEqual('Ingredient of type Purple not allowed in PaintFactory', str(ex.exception))

    def test_valid_ingredient_no_space_raises_ex(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 15)
        self.assertEqual('Not enough space in factory', str(ex.exception))

    def test_add_ingredient_if_product_and_quantity_are_valid(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 10}, self.paint_factory.ingredients)

    def test_remove_ingredient_not_existing_raises_ex(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('white', 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_when_quantity_goes_below_zero_raises_ex(self):
        self.paint_factory.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient('white', 10)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(ex.exception))

    def test_removes_correctly_added_ingredient(self):
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.remove_ingredient('white', 5)
        self.assertDictEqual({'white': 0}, self.paint_factory.ingredients)
        self.assertTrue('white' in self.paint_factory.ingredients)
        self.assertEqual(0, self.paint_factory.ingredients['white'])

    def test_proper_return_of_products(self):
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.add_ingredient('yellow', 5)
        result = self.paint_factory.products
        expected = {'white': 5, 'yellow': 5}
        self.assertEqual(expected, result)
        self.assertTrue('white' in self.paint_factory.products)
        self.assertTrue('yellow' in self.paint_factory.products)
        self.assertEqual(5, self.paint_factory.ingredients['white'])
        self.assertEqual(5, self.paint_factory.ingredients['yellow'])

    def test_str_method_returns_correctly(self):
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.add_ingredient('yellow', 5)
        result = str(self.paint_factory)
        expected = f"Factory name: Test with capacity 10.\nwhite: 5\nyellow: 5\n"
        self.assertEqual(expected, result)













if __name__ == '__main__':
    main()