from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    # CAKE_PORTION = 245

    def __init__(self, name: str, price: float):
        super(Cake, self).__init__(name, 245, price)
