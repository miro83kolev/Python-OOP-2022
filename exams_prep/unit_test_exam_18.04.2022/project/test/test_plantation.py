from project.plantation import Plantation

from unittest import TestCase, main


class PlantationTests(TestCase):

    def test_init_plantation(self):
        plantation = Plantation(1)

        self.assertEqual(1, plantation.size)
        self.assertListEqual([], plantation.workers)
        self.assertDictEqual({}, plantation.plants)

    def test_size_raises_error(self):
        plantation = Plantation(1)

        with self.assertRaises(ValueError) as context:
            plantation.size = -1
        self.assertEqual('Size must be positive number!', str(context.exception))

    def test_hire_worker_raises_exception_when_existing(self):
        plantation = Plantation(1)
        plantation.hire_worker('Pesho')
        with self.assertRaises(ValueError) as context:
            plantation.hire_worker('Pesho')
        self.assertEqual('Worker already hired!', str(context.exception))
        self.assertEqual(1, len(plantation.workers))
        self.assertTrue('Pesho' in plantation.workers)

    def test_hire_worker_not_existing(self):
        plantation = Plantation(1)
        worker_one = 'Pesho'
        plantation.hire_worker(worker_one)
        self.assertTrue(1, len(plantation.workers))
        worker_two = 'Ivan'
        result = plantation.hire_worker(worker_two)
        self.assertTrue(2, len(plantation.workers))
        self.assertTrue(worker_two in plantation.workers)
        success_msg = f'{worker_two} successfully hired.'
        self.assertEqual(result, success_msg)

    def test_count_increase_of_len_plants(self):
        plantation = Plantation(2)
        plantation.hire_worker('Pesho')
        plantation.plants['Pesho'] = ['Tomatoes']
        self.assertEqual(plantation.__len__(), 1)
        plantation.plants['Pesho'] = ['Tomatoes', 'Carrots']
        self.assertEqual(plantation.__len__(), 2)

    def test_planting_when_worker_not_existing(self):
        plantation = Plantation(1)
        with self.assertRaises(ValueError) as context:
            plantation.planting('Pesho', 'Carrots')
        self.assertEqual('Worker with name Pesho is not hired!', str(context.exception))

    def test_planing_when_plantation_full_raises(self):
        plantation = Plantation(1)
        plantation.hire_worker('Pesho')
        plantation.planting('Pesho', 'Tomatoes')
        with self.assertRaises(ValueError) as context:
            plantation.planting('Pesho', 'Carrots')
        self.assertEqual('The plantation is full!', str(context.exception))

    def test_planting_correctly_for_first_plant(self):
        plantation = Plantation(1)
        worker = "Pesho"
        plantation.hire_worker(worker)
        result = plantation.planting(worker, 'Tomatoes')
        sucess_msg = f"{worker} planted it's first Tomatoes."
        self.assertEqual(sucess_msg, result)
        self.assertDictEqual({'Pesho': ['Tomatoes']}, plantation.plants)

    def test_planting_correctly_for_second_plant(self):
        plantation = Plantation(2)
        worker = "Pesho"
        plantation.hire_worker(worker)
        plantation.planting(worker, 'Tomatoes')
        self.assertEqual(1, plantation.__len__())
        plant = 'Carrots'
        result = plantation.planting(worker, plant)
        sucess_msg = f"{worker} planted {plant}."
        self.assertEqual(sucess_msg, result)
        self.assertDictEqual({'Pesho': ['Tomatoes', 'Carrots']}, plantation.plants)
        self.assertTrue(2, plantation.__len__())

    def test_str_wrong_output(self):
        self.assertEqual(Plantation(2).__str__().strip(), 'Plantation size: 2')
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(self.pl.__str__().strip(), 'Plantation size: 2\nMartin\nMartin planted: Radishes')

    def test_repr_wrong_output(self):
        self.assertEqual(Plantation(2).__repr__().strip(), 'Size: 2\nWorkers:')
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.assertEqual(self.pl.__repr__().strip(), 'Size: 2\nWorkers: Martin')


    def test_len_wrong_count(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_wrong_iterable(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)



if __name__ == '__main__':
    main()
