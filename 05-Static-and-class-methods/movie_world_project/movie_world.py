from movie_world_project.customer import Customer
from movie_world_project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for cust in self.customers:
            result += cust.__repr__()+"\n"
        for dvd in self.dvds:
            result += dvd.__repr__()+"\n"
        return result


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
d3 = DVD("Lolita", 3, 1992, "March", 18)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)
movie_world.add_dvd(d3)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))
print(movie_world.rent_dvd(1, 3))

print(movie_world)

# John should be at least 18 to rent this movie
# Anna has successfully rented Black Widow
# John has successfully rented The Croods 2
# 1: John of age 16 has 1 rented DVD's (The Croods 2)
# 2: Anna of age 55 has 1 rented DVD's (Black Widow)
# 1: Black Widow (April 2020) has age restriction 18. Status: rented
# 2: The Croods 2 (December 2020) has age restriction 3. Status: rented
