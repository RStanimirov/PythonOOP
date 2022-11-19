from pizza_maker_project.topping import Topping
from pizza_maker_project.dough import Dough


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}
        self.counter = 0
        # test input: p = Pizza("Margherita", whole_wheat_dough, 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        else:
            self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        else:
            self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        else:
            self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        self.counter += 1
        if topping.topping_type not in self.toppings:
            if self.toppings_capacity >= self.counter:
                self.toppings[topping.topping_type] = topping.weight
            else:
                raise ValueError("Not enough space for another topping")
        else:
            if self.toppings_capacity >= self.counter:
                self.toppings[topping.topping_type] += topping.weight
            else:
                raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        toppings_weight = 0
        for x in self.toppings.values():
            toppings_weight += x
        total_weight_of_pizza = toppings_weight + self.dough.weight
        return total_weight_of_pizza


"""Sample input: """
tomato_topping = Topping("Tomato", 60)
print(tomato_topping.topping_type)
print(tomato_topping.weight)

mushrooms_topping = Topping("Mushroom", 75)
print(mushrooms_topping.topping_type)
print(mushrooms_topping.weight)

mozzarella_topping = Topping("Mozzarella", 80)
print(mozzarella_topping.topping_type)
print(mozzarella_topping.weight)

cheddar_topping = Topping("Cheddar", 150)

pepperoni_topping = Topping("Pepperoni", 120)

white_flour_dough = Dough("White Flour", "Mixing", 200)
print(white_flour_dough.flour_type)
print(white_flour_dough.weight)
print(white_flour_dough.baking_technique)

whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
print(whole_wheat_dough.weight)
print(whole_wheat_dough.flour_type)
print(whole_wheat_dough.baking_technique)

p = Pizza("Margherita", whole_wheat_dough, 2)

p.add_topping(tomato_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)

"""Sample output: """
# Tomato
# 60
# Mushroom
# 75
# Mozzarella
# 80
# White Flour
# 200
# Mixing
# 200
# Whole Wheat Flour
# Mixing
# 260
# 340
# ValueError: Not enough space for another topping
