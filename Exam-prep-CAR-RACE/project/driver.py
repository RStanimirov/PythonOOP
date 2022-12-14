class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None  # car: Car --> One driver drives ONLY one car.
        self.number_of_wins = 0  # When the driver wins a race, the number of wins should be increased!

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

