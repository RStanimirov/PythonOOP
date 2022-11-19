from lab_multiple_project.employee import Employee
from lab_multiple_project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
