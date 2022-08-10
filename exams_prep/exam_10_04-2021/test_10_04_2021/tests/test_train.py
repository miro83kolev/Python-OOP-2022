from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train('TrainName', 3)

    def test_init_train(self):
        name = 'Train'
        capacity = 3
        train = Train(name, capacity)

        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_passenger_and_returns_proper_string(self):
        passenger_name = 'Pesho'
        result = self.train.add(passenger_name)

        self.assertEqual(f'Added passenger {passenger_name}', result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_add_to_full_capacity_raises(self):
        self.train.passengers = ['Pesho', 'Gosho', 'Ivan']

        with self.assertRaises(ValueError) as context:
            self.train.add('Kotse')
        self.assertEqual('Train is full', str(context.exception))

    def test_add_to_train_when_passenger_exists_raises(self):
        passenger_name = 'Pesho'
        self.train.passengers = [passenger_name]
        with self.assertRaises(ValueError) as context:
            self.train.add(passenger_name)
        self.assertEqual(f'Passenger {passenger_name} Exists', str(context.exception))

    def test_remove_raises_when_passenger_does_not_exist(self):
        self.train.passengers = ['Pesho', 'Gosho', 'Ivan']

        with self.assertRaises(ValueError) as context:
            self.train.remove('Kotse')
        self.assertEqual('Passenger Not Found', str(context.exception))

    def test_removes_passenger_when_on_train(self):
        self.train.passengers = ['Pesho','Ivan']
        result = self.train.remove('Pesho')

        self.assertEqual('Removed Pesho', result)
        self.assertTrue('Pesho' not in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))
        self.assertTrue('Ivan' in self.train.passengers)


if __name__ == '__main__':
    main()