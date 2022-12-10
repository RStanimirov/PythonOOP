from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    comfort = 1
    price = 5

    def __init__(self):
        super(Ornament, self).__init__(self.comfort, self.price)


