from project.car.car import Car


class SportsCar(Car):
    # minimum speed limit is 400, and its maximum speed limit is 600 (inclusive)
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model, speed_limit):
        super(SportsCar, self).__init__(model, speed_limit)

    def get_min_speed_limit(self):
        return self.MIN_SPEED_LIMIT

    def get_max_speed_limit(self):
        return self.MAX_SPEED_LIMIT
