from project.plantation import Plantation

from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_init_plantation(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.plants))
        self.assertEqual(0, len(self.plantation.workers))

    def test_plantation_raises_error_when_size_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -20
        self.assertEqual('Size must be positive number!', str(ex.exception))

    def test_hire_worker_when_not_in_list(self):
        self.assertEqual(0, len(self.plantation.workers))
        self.plantation.hire_worker('Ivan')
        self.assertEqual(['Ivan'], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        self.assertTrue('Ivan' in self.plantation.workers)

    def test_hire_worker_returns_correct_str(self):
        result = self.plantation.hire_worker('Ivan')
        expected = 'Ivan successfully hired.'
        self.assertEqual(expected, result)

    def test_hire_worker_raises_ex_when_worker_already_in_list(self):
        self.plantation.hire_worker('Ivan')
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('Ivan')
        self.assertEqual('Worker already hired!', str(ex.exception))

    def test_len_returns_correctly(self):
        self.assertEqual(0, len(self.plantation.plants))
        self.plantation.plants = {'Ivan': ['Tomato', 'Apple'], 'Stoyan': ['Melon']}
        self.assertEqual(2, len(self.plantation.plants))
        self.assertEqual(3, len(self.plantation))

    def test_planting_when_worker_not_existing(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Ivan', 'Tomatoes')
        self.assertEqual('Worker with name Ivan is not hired!', str(ex.exception))

    def test_plantation_raises_when_full(self):
        self.plantation.size = 2
        self.plantation.hire_worker('Ivan')
        for index in range(2):
            self.plantation.planting('Ivan', 'Tomato' + str(index))

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Ivan", "Tomato3")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_if_space_and_worker_but_first_plant(self):
        self.plantation.hire_worker('Ivan')
        result = self.plantation.planting('Ivan', 'Tomato')
        self.assertDictEqual({'Ivan': ['Tomato']}, self.plantation.plants)
        self.assertEqual('Ivan planted it\'s first Tomato.', result)
        self.assertTrue('Ivan' in self.plantation.workers)
        self.assertTrue('Tomato' in self.plantation.plants['Ivan'])

    def test_planting_if_space_and_worker_in_plants(self):
        self.plantation.hire_worker("Adam")
        self.plantation.planting("Adam", "Peppers")
        result = self.plantation.planting("Adam", "Tomato")
        self.assertEqual({"Adam": ["Peppers", "Tomato"]}, self.plantation.plants)
        self.assertEqual(f"Adam planted Tomato.", result)
        self.assertTrue('Adam' in self.plantation.workers)
        self.assertTrue('Peppers' in self.plantation.plants['Adam'])
        self.assertTrue('Tomato' in self.plantation.plants['Adam'])

    def test_str_returns_correct_string(self):
        self.plantation.hire_worker("Adam")
        self.plantation.hire_worker("Peter")
        self.plantation.planting("Adam", "Tomato")
        self.plantation.planting("Adam", "Beans")
        self.plantation.planting("Peter", "Peppers")
        result = str(self.plantation)
        expected = "Plantation size: 5\n" \
                   "Adam, Peter\n" \
                   "Adam planted: Tomato, Beans\n" \
                   "Peter planted: Peppers"
        self.assertEqual(expected, result)

    def test_repr_returns_correct_string(self):
        self.plantation.hire_worker("Adam")
        self.plantation.hire_worker("Peter")
        result = repr(self.plantation)
        expected = 'Size: 5\nWorkers: Adam, Peter'

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
