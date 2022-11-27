from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.controller import Controller
from project.driver import Driver
from project.race import Race

nissan_car = MuscleCar("Nissan", 260)
ferrari_car = SportsCar("Ferrari", 420)

my_driver = Driver("Gawain")
other_driver = Driver("Nelson")

pernik_cup = Race("Pernik cup")
sofia_cup = Race("Sofia cup")

controller = Controller()
print(controller.create_car("MuscleCar", "Ford", 263))
print(controller.create_car("SportsCar", "Lamborghini", 520))
# print(controller.create_car("GreatCar", "Moskvich", 345))  # returns None
print(controller.create_driver("Pesho"))
print(controller.create_driver("Gosho"))
print(controller.create_race("Divotino cup"))
print(controller.create_race("Breznic race"))




