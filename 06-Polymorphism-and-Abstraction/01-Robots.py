class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')


# # below type cheking is nor desired, there should be a simpler, polymorhistic  way:
# def number_of_robot_sensors(robot):
#     if isinstance(robot, Robot):
#         print(robot.sensors_amount())
#     if isinstance(robot, MedicalRobot):
#         print(robot.medical_robot_sensors_amount())
#     elif isinstance(robot, ChefRobot):
#         print(robot.chef_robot_sensors_amount())
#     elif isinstance(robot, WarRobot):
#         print(robot.war_robot_sensors_amount())

# # below code got rid of the type-checking and applied a polymorphistic approach:
# def number_of_robot_sensors(robot):
#     print(robot.sensors_amount())
#
#
# number_of_robot_sensors(basic_robot)
# number_of_robot_sensors(da_vinci)
# number_of_robot_sensors(moley)
# number_of_robot_sensors(griffin)

# below is even a simpler way, no need to create a helper function:
print(basic_robot.sensors_amount())
print(da_vinci.sensors_amount())
print(moley.sensors_amount())
print(griffin.sensors_amount())
