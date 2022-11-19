from wild_cat_zoo_project.animal import Animal


class Cheetah(Animal):
    tend_requirements = 60

    def __init__(self, name, gender, age):
        super(Cheetah, self).__init__(name, gender, age)
        self.money_for_care = 60