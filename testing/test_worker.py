class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase, main

class WorkerTests(TestCase):
    def test_worker_is_initialized(self):
        #Tripple A - arange, act, assert
        worker = Worker("Test", 100, 10) #arrange and act together
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_increase(self):
        #arrange
        worker = Worker("Test", 100, 10) # build is instance of Worker
        #act
        self.assertEqual(10, worker.energy)
        worker.rest()
        #assert
        self.assertEqual(11, worker.energy)

    def test_worker_energy_0_raises(self):
        # arrange
        worker = Worker("Test", 100, 10)  # build is instance of Worker
        #assert, act
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_energy_negative_raises(self):
        # arrange
        worker = Worker("Test", 100, -1)  # build is instance of Worker
        # assert, act
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_is_payed(self):
        # arrange
        worker = Worker("Test", 100, 10)
        #act
        self.assertEqual(0, worker.money)
        worker.work()
        #assert
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_energy_decrease(self):
        # arrange
        worker = Worker("Test", 100, 10)
        # act
        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)
        worker.work()
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        # arrange
        worker = Worker("Test", 100, 10)

        result = worker.get_info()
        excepted = 'Test has saved 0 money.'
        self.assertEqual(excepted, result)

        worker.work()
        result = worker.get_info()
        excepted = 'Test has saved 100 money.'
        self.assertEqual(excepted, result)

if __name__ == '__main__':
    main()
















