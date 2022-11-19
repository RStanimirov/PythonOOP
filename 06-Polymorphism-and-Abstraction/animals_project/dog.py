from animals_project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Woof!"

    def __repr__(self):
        return Animal.__repr__(self)
