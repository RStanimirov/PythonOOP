from abc import ABC, abstractmethod


class BaseFish(ABC):
    EAT_INCREMENTAL = 5

    @abstractmethod
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

        # # RS tried with below code but got only 105/150 in Judge:
        # if self.name is '':
        #     raise ValueError("Fish name cannot be an empty string.")
        # if self.species is '':
        #     raise ValueError("Fish species cannot be an empty string.")
        # if self.price <= 0:
        #     raise ValueError(
        #         "Price cannot be equal to or below zero.")
        # # TODO: check if above should be done with getters and setters, as is shown below:

    # with below getters and setters got 111/150 in Judeg:
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value == '':
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.EAT_INCREMENTAL


