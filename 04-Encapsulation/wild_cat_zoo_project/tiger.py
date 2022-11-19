from wild_cat_zoo_project.animal import Animal


class Tiger(Animal):
    tend_requirements = 45

    def __init__(self, name, gender, age):
        super(Tiger, self).__init__(name, gender, age)
        self.money_for_care = 45