from project.plantation import Plantation

from unittest import TestCase, main


class PlantationTestCase(TestCase):
    SIZE = 10

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_setter_size_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = -10
        self.assertEqual('Size must be positive number!', str(context.exception))

    def test_hire_worker_not_list(self):
        first_name = 'Pesho'
        second_name = 'Gosho'

        self.plantation.hire_worker(first_name)
        result = f'{first_name} successfully hired.'
        self.assertEqual('Pesho successfully hired.', result)
        self.plantation.hire_worker(second_name)
        result_two = f'{second_name} successfully hired.'
        self.assertEqual('Gosho successfully hired.', result_two)

        self.assertEqual([first_name, second_name], self.plantation.workers)
        self.assertTrue(2, len(self.plantation.workers))

    def test_hire_worker_raises_exception_when_in_the_list(self):
        first_name = 'Pesho'
        second_name = 'Gosho'

        self.plantation.hire_worker(first_name)
        self.plantation.hire_worker(second_name)

        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker(first_name)
        self.assertEqual('Worker already hired!', str(context.exception))
        self.assertTrue(2, len(self.plantation.workers))









if __name__ == '__main__':
    main()
