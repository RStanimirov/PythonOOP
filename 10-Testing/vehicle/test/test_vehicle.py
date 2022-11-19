import unittest

from vehicle.project.vehicle import Vehicle
# from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def test_init(self):
        my_car = Vehicle(22.0, 110.0)
        self.assertEqual(22.0, my_car.fuel)
        self.assertEqual(110.0, my_car.horse_power)

    def test_drive_raise_exception(self):
        my_car = Vehicle(2.0, 110.0)
        with self.assertRaises(Exception) as ex:
            my_car.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        my_car = Vehicle(20.0, 110.0)
        my_car.drive(10)
        remaining_fuel = 20.0 - (1.25 * 10)
        self.assertEqual(remaining_fuel, my_car.fuel)

    def test_refuel_too_much_fuel_raise_exception(self):
        my_car = Vehicle(20.0, 110.0)
        my_car.drive(10)
        with self.assertRaises(Exception) as ex:
            my_car.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_sucessful(self):
        my_car = Vehicle(20.0, 110.0)
        my_car.drive(10)
        my_car.refuel(4)
        self.assertEqual(11.5, my_car.fuel)

    def test_str(self):
        my_car = Vehicle(20.0, 110.0)
        my_car.drive(10)
        my_car.refuel(4)
        result = "The vehicle has 110.0 horse power with 11.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, my_car.__str__())


if __name__ == '__main__':
    unittest.main()