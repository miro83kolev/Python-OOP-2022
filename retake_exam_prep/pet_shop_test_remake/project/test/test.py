from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Test')

    def test_init_pet_shop(self):
        self.assertEqual('Test', self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)
        self.assertEqual(0, len(self.pet_shop.food))
        self.assertEqual(0, len(self.pet_shop.pets))

    def test_raises_if_quantity_under_zero(self):
        for quantity in range(-5, 0):
            with self.assertRaises(ValueError) as ex:
                self.pet_shop.add_food('test food', quantity)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_adds_food_not_existing(self):
        self.pet_shop.add_food('dog food', 10)
        self.assertDictEqual({'dog food': 10}, self.pet_shop.food)
        self.assertTrue('dog food' in self.pet_shop.food)
        self.assertEqual(10, self.pet_shop.food['dog food'])

    def test_increase_of_adding_food(self):
        self.pet_shop.add_food('dog food', 10)
        self.pet_shop.add_food('dog food', 10)
        self.assertDictEqual({'dog food': 20}, self.pet_shop.food)
        self.assertEqual(20, self.pet_shop.food['dog food'])
        self.pet_shop.add_food('dog food', 10)
        self.assertDictEqual({'dog food': 30}, self.pet_shop.food)
        self.assertEqual(30, self.pet_shop.food['dog food'])

    def test_add_food_returns_proper_string(self):
        result = self.pet_shop.add_food('dog food', 10)
        expected = 'Successfully added 10.00 grams of dog food.'
        self.assertEqual(expected, result)

    def test_adding_pet_which_exists(self):
        self.pet_shop.add_pet("Koki")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Koki")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_adding_pets_works_correctly(self):
        self.pet_shop.add_pet("Koki")
        self.assertListEqual(['Koki'], self.pet_shop.pets)
        self.assertEqual(1, len(self.pet_shop.pets))
        self.pet_shop.add_pet('Boki')
        self.assertListEqual(['Koki', 'Boki'], self.pet_shop.pets)
        self.assertEqual(2, len(self.pet_shop.pets))

    def test_adding_returns_proper_string(self):
        result = self.pet_shop.add_pet("Koki")
        expected = 'Successfully added Koki.'
        self.assertEqual(expected, result)

    def test_feed_when_pet_not_found(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_food('dog food', 100)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('Cat food', 'Mimi')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_when_food_not_found(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_food('dog food', 100)
        result = self.pet_shop.feed_pet('Cat food', 'Koki')
        self.assertEqual('You do not have Cat food', result)
        self.assertTrue('Cat food' not in self.pet_shop.food)

    def test_feed_when_food_less_than_100(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_food('dog food', 99)
        result = self.pet_shop.feed_pet('dog food', 'Koki')
        self.assertEqual(1099.00, self.pet_shop.food['dog food'])
        self.assertEqual('Adding food...', result)
        self.assertDictEqual({'dog food': 1099}, self.pet_shop.food)

    def test_food_decrease_correctly(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_food('dog food', 500)
        self.pet_shop.feed_pet('dog food', 'Koki')
        self.assertEqual(400, self.pet_shop.food['dog food'])
        self.pet_shop.feed_pet('dog food', 'Koki')
        self.assertEqual(300, self.pet_shop.food['dog food'])

    def test_string_when_pet_correctly_fed(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_food('dog food', 500)
        result = self.pet_shop.feed_pet('dog food', 'Koki')
        expected = 'Koki was successfully fed'
        self.assertEqual(expected, result)

    def test_repr_returns_correct(self):
        self.pet_shop.add_pet('Koki')
        self.pet_shop.add_pet('Moki')
        expected = f'Shop Test:\nPets: Koki, Moki'
        result = repr(self.pet_shop)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
