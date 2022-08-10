from project.pet_shop import PetShop

from unittest import TestCase, main

class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Shop')

    def test_init_pet_shop(self):
        self.assertEqual('Shop', self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food_quantity_less_than_zero(self):
        self.pet_shop.food['food'] = 0
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food(self.pet_shop.food['food'], -10)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_when_name_not_existing(self):
        self.pet_shop.food['food'] = 0
        self.assertEqual(1, len(self.pet_shop.food))
        self.assertTrue('food' in self.pet_shop.food)
        self.assertEqual(0, self.pet_shop.food['food'])

    def test_add_food_increase_quantity(self):
        self.pet_shop.food['food'] = 0
        self.assertEqual(0, self.pet_shop.food['food'])
        result = self.pet_shop.add_food('food', 10)
        self.assertEqual(10, self.pet_shop.food['food'])
        self.assertEqual(f"Successfully added 10.00 grams of food.", result)

    def test_add_pet_when_not_in_list(self):
        result = self.pet_shop.add_pet('Gosho')
        self.assertEqual(1, len(self.pet_shop.pets))
        self.assertTrue('Gosho' in self.pet_shop.pets)
        self.assertEqual('Successfully added Gosho.', result)

    def test_add_pet_when_in_list_raises_exception(self):
        self.pet_shop.add_pet('Gosho')
        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet('Gosho')
        self.assertEqual('Cannot add a pet with the same name', str(context.exception))

    def test_feed_pet_raises_exception_when_pet_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet('food', 'pet1')
        self.assertEqual('Please insert a valid pet name', str(context.exception))

    def test_feed_pet_raises_exception_when_food_does_not_exist(self):
        self.pet_shop.add_pet('Gosho')
        result = self.pet_shop.feed_pet('food', 'Gosho')
        self.assertEqual('You do not have food', result)

    def test_feed_99_food_adding_and_return_correct_message(self):
        self.pet_shop.add_pet('Gosho')
        self.pet_shop.add_food('food', 99)
        result = self.pet_shop.feed_pet('food', 'Gosho')
        self.assertEqual(99 + 1000, self.pet_shop.food['food'])
        self.assertEqual('Adding food...', result)

    def test_feed_101_food_adding_and_return_correct_message(self):
        self.pet_shop.add_pet('Gosho')
        self.pet_shop.add_food('food', 101)
        result = self.pet_shop.feed_pet('food', 'Gosho')
        self.assertEqual(101 - 100, self.pet_shop.food['food'])
        self.assertEqual('Gosho was successfully fed', result)

    def test_repr_returns_correct(self):
        result = repr(self.pet_shop)
        self.pet_shop.add_pet('Gosho')
        self.pet_shop.add_pet('Pesho')
        self.pet_shop.add_pet('Stoyan')
        expected = f'Shop {self.pet_shop.name}:\n' + \
               f'Pets: Gosho, Pesho, Stoyan'

    def test_repr_returns_correct_when_no_pets(self):
        expected = f'''Shop {self.pet_shop.name}:
Pets: '''
        actual = repr(self.pet_shop)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
