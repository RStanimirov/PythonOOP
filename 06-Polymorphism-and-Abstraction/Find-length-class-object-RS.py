# RS a method to find the length, i.e number of parameters of a class object:
class Person(object):
    all_persons_list = []

    # below __repr__ prints the all_persons_list:
    # def __repr__(self):
    #     return str (self)

    def __init__(self, *args):
        # self.name = name
        # self.age = age
        # self.profession = profession
        # person_parameters_list = [self.name, self.age, self.profession]
        self.args = args
        person_parameters_list = [x for x in self.args]
        self.object_length = len(person_parameters_list)

    # finding the length is done by manipulating the __len__ :
    def __len__(self, *args):
        return self.object_length

    def __str__(self):
        # return f"This is {self.name} who is a {self.age}-year old {self.profession}."
        if self.object_length == 1:
            return f"This is {self.args[0]}."
        elif self.object_length == 2:
            return f"This is {self.args[0]} who is {self.args[1]} years old."
        elif self.object_length == 3:
            return f"This is {self.args[0]} who is a {self.args[1]}-year old {self.args[2]}."
        elif self.object_length == 4:
            return f"This is {self.args[0]} who is a {self.args[1]}-year old {self.args[2]} and a {self.args[3]}."
        else:
            return "This instantiation has more than 4 parameters. Please reformat accordingly."


p = Person("Ivan", 34, "engineer")
Person.all_persons_list.append(p)
p1 = Person("Dragan", 38, "manager", "a good fellow")
Person.all_persons_list.append(p1)
p2 = Person("Petkan", 28)
Person.all_persons_list.append(p2)
p3 = Person("Rick", 44, "consultant", "an experianced professional", "part-time")
Person.all_persons_list.append(p3)
# print(Person.all_persons_list)

# print(p)
# print(f"There are total {len(p)} parameters of this person's instantiation.")
# print(p1)
# print(f"There are total {len(p1)} parameters of this person's instantiation.")
# print(p2)
# print(f"There are total {len(p2)} parameters of this person's instantiation.")
# print(p3)
# print(f"There are total {len(p3)} parameters of this person's instantiation.")

for x in Person.all_persons_list:
    print(x)
    print(f"--> total {len(x)} parameters of this person's instantiation")