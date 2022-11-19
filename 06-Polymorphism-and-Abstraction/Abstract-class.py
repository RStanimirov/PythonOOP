from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()
dog = Dog("Willy")
dog.sound()
animal = Animal("Willy")
animal.sound()
# Meow!
# Bark!
# Error!
