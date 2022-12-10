from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # the number of fish the aquarium can have
        self.decorations = []  # will contain all decorations(objects)
        self.fish = []  # will contain all fish (objects)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        # return sum(decoration.comfort for decoration in self.decorations)
        summed_comfort = 0
        for x in self.decorations:
            summed_comfort += x.comfort
        return summed_comfort

    def add_fish(self, fish):
        if self.capacity < fish.size:
            return "Not enough capacity."
        else:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for x in self.fish:
            x.eat()

    def __str__(self):
        fish_names = [x.name for x in self.fish]
        if not self.fish:
            fish_names = None
        return f"{self.name}:\n" \
               f"Fish: {' '.join(fish_names)}\n" \
               f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
