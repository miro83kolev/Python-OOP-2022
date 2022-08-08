from unittest import TestCase, main

from project.survivor import Survivor


class SurvivorTests(TestCase):
    def test_set_att(self):
        survivor = Survivor('Test', 10)
        self.assertEqual(survivor.name, 'Test')
        self.assertEqual(survivor.age, 10)
        self.assertEqual(survivor.needs, 100)
        self.assertEqual(survivor.health, 100)
        self.assertFalse(survivor.needs_sustenance, False)
        self.assertFalse(survivor.needs_healing, False)

    def test_name_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            survivor = Survivor('', 10)
        self.assertEqual('Name not valid!', str(context.exception))

    def test_age_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            survivor = Survivor('Test', -10)
        self.assertEqual('Age not valid!', str(context.exception))

    def test_health_raises_exception(self):
        survivor = Survivor('Test', 10)
        with self.assertRaises(ValueError) as context:
            survivor.health = -50
        self.assertEqual('Health not valid!', str(context.exception))

    def test_needs_raises_exception(self):
        survivor = Survivor('Test', 10)
        with self.assertRaises(ValueError) as context:
            survivor.needs = - 50
        self.assertEqual('Needs not valid!', str(context.exception))

    def test_health_not_over_100(self):
        survivor = Survivor('Test', 10)
        survivor.health -= 20
        survivor.health += 30
        self.assertEqual(survivor.health, 100)

    def test_needs_not_over_100(self):
        survivor = Survivor('Test', 10)
        survivor.needs -= 20
        survivor.needs += 30
        self.assertEqual(survivor.needs, 100)

    def test_needs_sustain(self):
        survivor = Survivor('Test', 10)
        survivor.needs -= 20
        self.assertEqual(survivor.needs_sustenance, True)

    def test_needs_healing(self):
        survivor = Survivor('Test', 10)
        survivor.health -= 20
        self.assertEqual(survivor.needs_healing, True)

if __name__ == '__main__':
    main()
