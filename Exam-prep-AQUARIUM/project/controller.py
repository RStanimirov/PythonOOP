from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []  # will contain all aquariums (objects)

    # below is RS solution:
    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            aquarium_obj = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium_obj)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            aquarium_obj = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium_obj)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    # below is RS solution:
    def add_decoration(self, decoration_type):
        if decoration_type == "Ornament":
            decor_obj = Ornament()
            self.decorations_repository.add(decor_obj)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decor_obj = Plant()
            self.decorations_repository.add(decor_obj)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    # below code is RS solution - should be checked as slightly differs from other solutions:
    def insert_decoration(self, aquarium_name, decoration_type):
        current_decoration = self.decorations_repository.find_by_type(decoration_type)
        if len(self.aquariums) > 0:
            current_aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        else:
            current_aquarium = None
        if current_decoration is not "None" and current_aquarium is not None:
            current_aquarium.add_decoration(current_decoration)
            self.decorations_repository.remove(current_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        if current_decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

    # below code is RS solution - should be checked as slightly differs from other solutions:
    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if len(self.aquariums) > 0:
            current_aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        else:
            current_aquarium = None
        valid_fish = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type in valid_fish:
            if fish_type == 'FreshwaterFish':
                fish = FreshwaterFish(fish_name, fish_species, price)
                if current_aquarium.water != fish.water:
                    return "Water not suitable."
                if current_aquarium.capacity < FreshwaterAquarium.capacity:
                    return "Not enough capacity."
                return current_aquarium.add_fish(fish)
            elif fish_type == 'SaltwaterFish':
                fish = SaltwaterFish(fish_name, fish_species, price)
                if current_aquarium.water != fish.water:
                    return "Water not suitable."
                if current_aquarium.capacity < SaltwaterAquarium.capacity:
                    return "Not enough capacity."
                return current_aquarium.add_fish(fish)
        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name):
        # current_aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        for x in self.aquariums:
            if x.name == aquarium_name:
                current_aquarium = x
                current_aquarium.feed()
                return f"Fish fed: {len(current_aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        current_aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        fish_price = sum(fish.price for fish in current_aquarium.fish)
        decorations_price = sum(decoration.price for decoration in current_aquarium.decorations)
        total_price = fish_price + decorations_price
        return f"The value of Aquarium {aquarium_name} is {total_price:.2f}."

    def report(self):
        # return "\n".join(str(aquarium) for aquarium in self.aquariums)
        result = ""
        # for aquarium in self.aquariums:
        #     result += aquarium.__str__()
        for aquarium in self.aquariums:
            result += aquarium.__str__() + '\n'
        return result.strip()

