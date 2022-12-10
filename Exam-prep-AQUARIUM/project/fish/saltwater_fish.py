from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size = 5
    water = "Fresh"
    EAT_INCREMENTAL = 2

    def __init__(self, name, species, price):
        super(SaltwaterFish, self).__init__(name, species, self.size, price)
