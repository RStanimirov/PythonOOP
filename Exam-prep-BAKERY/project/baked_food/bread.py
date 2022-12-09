from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    # BREAD_PORTION = 200

    def __init__(self, name: str, price: float):
        super(Bread, self).__init__(name, 200, price)
