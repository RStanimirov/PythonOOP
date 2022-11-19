from abc import ABC, abstractmethod, abstractproperty


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Worker(Person):
    # def __init__(self, name, age):
    #     super(Worker, self).__init__(name, age)
    #     self.name = name
    #     self.age = age
    pass


worker = Worker("Pesho", 32)
print(worker.name)

