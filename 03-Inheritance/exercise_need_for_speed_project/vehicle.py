class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        required_fuel = kilometers * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel


# vehicle = Vehicle(50, 150)
# print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
# print(vehicle.fuel)
# print(vehicle.horse_power)
# print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)
# family_car = FamilyCar(150, 150)
# family_car.drive(50)
# print(family_car.fuel)
# family_car.drive(50)
# print(family_car.fuel)
# print(family_car.__class__.__bases__[0].__name__)

