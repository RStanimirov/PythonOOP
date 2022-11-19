from restaurant_project.beverage.beverage import Beverage
from restaurant_project.beverage.coffee import Coffee
from restaurant_project.food.soup import Soup


class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, value):
    #     self.__name = value

    @property
    def price(self):
        return self.__price

    # @price.setter
    # def price(self, value):
    #     self.__price = value


product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)

"""Below test code is supplementary (RS), not included in the task's test inputs"""
coffee = Coffee("Espresso", 3.34)
print(coffee.__class__.__name__)
print(coffee.__class__.__bases__[0].__name__)
print(coffee.name)
print(coffee.price)
print(coffee.milliliters)
print(coffee.caffeine)