import unittest

from mammal.project.mammal import Mammal
# from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_correct_initialisation(self):
        mammal = Mammal("Monkey", "primate", "shriek")
        self.assertEqual("Monkey", mammal.name)
        self.assertEqual("primate", mammal.type)
        self.assertEqual("shriek", mammal.sound)

    def test_make_sound(self):
        mammal = Mammal("Monkey", "primate", "shriek")
        result = mammal.make_sound()
        self.assertEqual("Monkey makes shriek", result)

    def test_get_kingdom(self):
        mammal = Mammal("Monkey", "primate", "shriek")
        result = mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        mammal = Mammal("Monkey", "primate", "shriek")
        result = mammal.info()
        self.assertEqual("Monkey is of type primate", result)


if __name__ == '__main__':
    unittest.main()
