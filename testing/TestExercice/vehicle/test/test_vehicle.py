from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_vehicle_init(self):
        fuel = 100
        horse_power = 150
        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_vehicle_str_returns_proper_string(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        actual_result = str(self.vehicle)
        self.assertEqual(expected_result, actual_result)

    def test_drive_raises_when_distance_not_reachable(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(context.exception))

    def test_drive_reduces_fuel(self):
        distance = 10
        burned_fuel = distance * self.vehicle.fuel_consumption
        expected_result = self.vehicle.fuel - burned_fuel
        self.vehicle.drive(distance)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_fuel_raises_when_full(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)
        self.assertEqual('Too much fuel', str(context.exception))

    def test_fuel_when_not_full(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)
        self.assertEqual(100, self.vehicle.fuel)







if __name__ == '__main__':
    main()