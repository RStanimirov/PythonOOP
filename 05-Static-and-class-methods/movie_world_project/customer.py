class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvds = ', '.join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} " \
               f"has {len(self.rented_dvds)} " \
               f"rented DVD's ({rented_dvds})"