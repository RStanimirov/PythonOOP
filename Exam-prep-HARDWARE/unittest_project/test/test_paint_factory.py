import unittest

from unittest_project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def test_init(self):
        art_studio = PaintFactory("Art Studio", 10)
        self.assertEqual("Art Studio", art_studio.name)
        self.assertEqual(10, art_studio.capacity)
        self.assertEqual(['white', 'yellow', 'blue', 'green', 'red'], art_studio.valid_ingredients)

    def test_add_ingredient_raise_type_error(self):
        art_studio = PaintFactory("Art Studio", 10)
        with self.assertRaises(TypeError) as ex:
            art_studio.add_ingredient("magenta", 6)
        self.assertEqual("Ingredient of type magenta not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_valid(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        self.assertEqual({'red': 5}, art_studio.ingredients)
        art_studio.add_ingredient("red", 3)
        self.assertEqual({'red': 8}, art_studio.ingredients)
        art_studio.add_ingredient("blue", 2)
        self.assertEqual({'red': 8, 'blue': 2}, art_studio.ingredients)

    def test_add_ingredient_not_enough_space(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        with self.assertRaises(ValueError) as ex:
            art_studio.add_ingredient("blue", 2)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_can_add_method(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 1)
        self.assertTrue(art_studio.can_add(1), True)

    def test_remove_ingredient_raise_value_error(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        with self.assertRaises(ValueError) as ex:
            art_studio.remove_ingredient("blue", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_valid(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        art_studio.remove_ingredient("blue", 2)
        self.assertEqual({'red': 8, 'blue': 0}, art_studio.ingredients)
        # self.assertEqual(None, art_studio.remove_ingredient("blue", 2))

    def test_remove_ingredient_raise_key_error(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        with self.assertRaises(KeyError) as ex:
            art_studio.remove_ingredient("magenta", 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_repr_method(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        print_str = "Factory name: Art Studio with capacity 10.\nred: 8\nblue: 2\n"
        self.assertEqual(print_str, art_studio.__repr__())

    def test_products_property(self):
        art_studio = PaintFactory("Art Studio", 10)
        art_studio.add_ingredient("red", 5)
        art_studio.add_ingredient("red", 3)
        art_studio.add_ingredient("blue", 2)
        self.assertEqual({'red': 8, 'blue': 2}, art_studio.products)


if __name__ == '__main__':
    unittest.main()
