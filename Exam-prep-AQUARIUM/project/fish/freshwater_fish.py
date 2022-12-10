from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size = 3
    water = "Fresh"
    EAT_INCREMENTAL = 3

    def __init__(self, name, species, price):
        super(FreshwaterFish, self).__init__(name, species, self.size, price)
