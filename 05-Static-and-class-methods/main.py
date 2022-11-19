class Holiday:
    def __init__(self, name, flowers):
        self.name = name
        self.flowers = flowers
        self.kisses = True

    @staticmethod
    def present_flower(rose, tulips, daffodils):
        return f"Happy 8th March ! Accept these f{rose}, {tulips}, {daffodils}"

    def __str__(self):
        return f"This celebrations is {self.name} and gentlemen are expected " \
               f"to endow the ladies with lots of {self.flowers}."


march_celebration = Holiday("Women's Day", ["tulips", "snowdrops", "carnations"])
print(march_celebration)
