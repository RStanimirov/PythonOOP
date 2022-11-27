from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        # valid car types are "MuscleCar" and "SportsCar"
        if car_type == "MuscleCar":
            if self.cars:
                for x in self.cars:
                    if x.model == model:
                        raise Exception(f"Car {model} is already created!")
                    else:
                        new_muscle_car = MuscleCar(model, speed_limit)
                        self.cars.append(new_muscle_car)
                        return f"{car_type} {model} is created."
            else:
                new_muscle_car = MuscleCar(model, speed_limit)
                self.cars.append(new_muscle_car)
                return f"{car_type} {model} is created."

        elif car_type == "SportsCar":
            if self.cars:
                for x in self.cars:
                    if x.model == model:
                        raise Exception(f"Car {model} is already created!")
                    else:
                        new_sports_car = SportsCar(model, speed_limit)
                        self.cars.append(new_sports_car)
                        return f"{car_type} {model} is created."
            else:
                new_sports_car = SportsCar(model, speed_limit)
                self.cars.append(new_sports_car)
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.drivers:
            for x in self.drivers:
                if x.name == driver_name:
                    raise Exception(f"Driver {driver_name} is already created!")
                else:
                    new_driver = Driver(driver_name)
                    self.drivers.append(new_driver)
                    return f"Driver {driver_name} is created."
        else:
            new_driver = Driver(driver_name)
            self.drivers.append(new_driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.races:
            for x in self.races:
                if x.name == race_name:
                    raise Exception(f"Race {race_name} is already created!")
                else:
                    new_race = Race(race_name)
                    self.races.append(new_race)
                    return f"Race {race_name} is created."
        else:
            new_race = Race(race_name)
            self.races.append(new_race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        for x in self.drivers:
            if x.name == driver_name:
                if self.cars:
                    if car_type == "MuscleCar":
                        last_muscle_car = [x for x in self.cars][-1]
                        if driver_name.car is not None:
                            old_model = driver_name.car
                            driver_name.car = last_muscle_car
                            return f"Driver {driver_name} changed his car from {old_model} to {last_muscle_car}."
                        else:
                            driver_name.car = last_muscle_car
                    elif car_type == "SportsCar":
                        last_sports_car = [x for x in self.cars][-1]
                        if driver_name.car is not None:
                            old_model = driver_name.car
                            driver_name.car = last_sports_car
                            return f"Driver {driver_name} changed his car from {old_model} to {last_sports_car}."
                        else:
                            driver_name.car = last_sports_car
                else:
                    raise Exception(f"Car {car_type} could not be found!")
            else:
                raise Exception(f"Driver {driver_name} could not be found!")
        raise Exception(f"Driver {driver_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        for x in self.races:
            if x.name == race_name:
                for drvr in self.drivers:
                    if drvr.name == driver_name:
                        if drvr.car is not None:
                            if driver_name in self.races:
                                return f"Driver {driver_name} is already added in {race_name} race."
                            self.races.append(driver_name)
                            return f"Driver {driver_name} added in {race_name} race."
                        else:
                            raise Exception(f"Driver {driver_name} could not participate in the race!")
                    raise Exception(f"Driver {driver_name} could not be found!")
                raise Exception(f"Driver {driver_name} could not be found!")
        raise Exception(f"Race {race_name} could not be found!")

    def start_race(self, race_name: str):
        for x in self.races:
            if x.name == race_name:
                if len(self.races) < 3:
                    raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
                elif len(self.races) >= 3:
                    race_1 = self.create_race(race_name)
                    winners = sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]
                    result = ''
                    for driver in winners:
                        driver.number_of_wins += 1
                        result += f'Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n'
                    return result.strip()
            else:
                raise Exception(f"Race {race_name} could not be found!")
        raise Exception(f"Race {race_name} could not be found!")

