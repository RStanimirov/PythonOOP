from project.controller import Controller
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish

family_aquarium = FreshwaterAquarium("Family aquarium")
yellow_goldfish = FreshwaterFish("Yellow goldfish", "Goldfish", 2.50)
red_goldfish = FreshwaterFish("Red goldfish", "Goldfish", 2.40)
blue_goldfish = FreshwaterFish("Blue goldfish", "Goldfish", 2.30)
aqua_rocks = Ornament()
aqua_plant = Plant()
controller = Controller()
print(family_aquarium.add_fish(yellow_goldfish))
print(family_aquarium.add_fish(red_goldfish))
print(family_aquarium.add_decoration(aqua_rocks))
print(family_aquarium.add_decoration(aqua_plant))
print(family_aquarium)
print(controller.add_aquarium("FreshwaterAquarium", "Family aquarium"))
print(controller.add_fish("Family aquarium", "FreshwaterFish", "Blue goldfish", "Goldfish", 2.30))
print(controller.report())
