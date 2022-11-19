from gym_project.customer import Customer
from gym_project.exercise_plan import ExercisePlan
from gym_project.trainer import Trainer
from gym_project.equipment import Equipment
from gym_project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self. customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        # subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        # customer = [x for x in self.customers if x.id == subscription_id][0]
        # trainer = [x for x in self.trainers if x.id == subscription_id][0]
        # equipment = [x for x in self.equipment if x.id == subscription_id][0]
        # plan = [x for x in self.plans if x.id == subscription_id][0]

        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = [x for x in self.customers if x.id == subscription.customer_id][0]
        trainer = [x for x in self.trainers if x.id == subscription.trainer_id][0]
        plan = [x for x in self.plans if x.id == subscription.exercise_id][0]
        equipment = [x for x in self.equipment if x.id == plan.equipment_id][0]

        return f"{subscription.__repr__()}\n" + f"{customer.__repr__()}\n" + f"{trainer.__repr__()}\n" + f"{equipment.__repr__()}\n" + f"{plan.__repr__()}"


# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
# gym = Gym()
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
# print(Customer.get_next_id())
# print(gym.subscription_info(1))

# 2
# Subscription <1> on 14.05.2020
# Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
# Trainer <1> Peter
# Equipment <1> Treadmill
# Plan <1> with duration 20 minutes
