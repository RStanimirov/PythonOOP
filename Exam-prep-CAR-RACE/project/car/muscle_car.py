from project.car.car import Car


class MuscleCar(Car):
    # minimum speed limit is 250, and its maximum speed limit is 450 (inclusive)
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model, speed_limit):
        super(MuscleCar, self).__init__(model, speed_limit)

    def get_min_speed_limit(self):
        return self.MIN_SPEED_LIMIT

    def get_max_speed_limit(self):
        return self.MAX_SPEED_LIMIT
