from wild_cat_zoo_project.animal import Animal


class Lion(Animal):
    tend_requirements = 50

    def __init__(self, name, gender, age):
        super(Lion, self).__init__(name, gender, age)
        self.money_for_care = 50


