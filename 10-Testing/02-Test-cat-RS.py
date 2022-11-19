class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def test_cat_size_increased_after_eating(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_is_fed(self):
        cat = Cat("Tom")
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_raise_error(self):
        cat = Cat("Tom")
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_fall_asleep_raise_error(self):
        cat = Cat("Tom")
        cat.fed = False
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_not_sleepy(self):
        cat = Cat("Tom")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()