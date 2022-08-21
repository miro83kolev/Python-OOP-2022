from unittest import TestCase, main

from project.train.train import Train

class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train('Test', 10)

    def test_init_train(self):
        self.assertEqual('Test', self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertListEqual([], self.train.passengers)
        self.assertEqual(0, len(self.train.passengers))

    def test_add_raises_exception_when_train_full(self):
        self.train.capacity = 2
        self.train.add('A')
        self.train.add('B')
        self.assertEqual(2, len(self.train.passengers))
        with self.assertRaises(ValueError) as ex:
            self.train.add('C')
        self.assertEqual('Train is full', str(ex.exception))

    def test_raises_exception_if_passenger_exists(self):
        self.train.capacity = 3
        self.train.add('A')
        self.train.add('B')
        self.assertEqual(2, len(self.train.passengers))
        with self.assertRaises(ValueError) as ex:
            self.train.add('A')
        self.assertEqual('Passenger A Exists', str(ex.exception))

    def test_add_method_adds_correctly(self):
        self.train.capacity = 3
        result = self.train.add('A')
        self.assertEqual(1, len(self.train.passengers))
        self.assertTrue('A' in self.train.passengers)
        self.assertEqual('Added passenger A', result)
        result = self.train.add('B')
        self.assertEqual(2, len(self.train.passengers))
        self.assertTrue('B' in self.train.passengers)
        self.assertEqual('Added passenger B', result)

    def test_remove_raises_exception_if_passenger_not_existing(self):
        self.train.capacity = 3
        with self.assertRaises(ValueError) as ex:
            self.train.remove('A')
        self.assertEqual('Passenger Not Found', str(ex.exception))
        self.assertEqual(0, len(self.train.passengers))
        self.assertFalse('A' in self.train.passengers)

    def test_remove_correctly_added_passenger(self):
        self.train.capacity = 3
        self.train.add('A')
        self.train.add('B')
        self.train.add('C')
        self.assertEqual(3, len(self.train.passengers))
        result = self.train.remove('A')
        self.assertEqual(2, len(self.train.passengers))
        self.assertEqual('Removed A', result)
        self.assertFalse('A' in self.train.passengers)
        result = self.train.remove('B')
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual('Removed B', result)
        self.assertFalse('B' in self.train.passengers)


if __name__ == '__main__':
    pass

