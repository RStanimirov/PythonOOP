from unittest_project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def test_correct_init(self):
        my_pet_shop = PetShop("Sweet Pets")
        self.assertEqual("Sweet Pets", my_pet_shop.name)
        self.assertEqual({}, my_pet_shop.food)
        self.assertEqual([], my_pet_shop.pets)

    def test_add_food_raise_value_error(self):
        my_pet_shop = PetShop("Sweet Pets")
        with self.assertRaises(ValueError) as ex:
            my_pet_shop.add_food("Bone", -2.0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_successful(self):
        my_pet_shop = PetShop("Sweet Pets")
        result = my_pet_shop.add_food("Bone", 2.0)
        self.assertEqual("Successfully added 2.00 grams of Bone.", result)
        self.assertEqual(my_pet_shop.food, {"Bone": 2.0})
        result = my_pet_shop.add_food("Bone", 1.0)
        self.assertEqual("Successfully added 1.00 grams of Bone.", result)
        self.assertEqual(my_pet_shop.food, {"Bone": 3.0})

    def test_add_pet_raise_exception(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_pet("Silver")
        with self.assertRaises(Exception) as ex:
            my_pet_shop.add_pet("Rex")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_successful(self):
        my_pet_shop = PetShop("Sweet Pets")
        result = my_pet_shop.add_pet("Rex")
        self.assertEqual("Successfully added Rex.", result)
        self.assertEqual(["Rex"], my_pet_shop.pets)
        result = my_pet_shop.add_pet("Silver")
        self.assertEqual("Successfully added Silver.", result)
        self.assertEqual(["Rex", "Silver"], my_pet_shop.pets)

    def test_feed_pet_raise_exception(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_food("Bone", 1000.0)
        with self.assertRaises(Exception) as ex:
            my_pet_shop.feed_pet("Bone", "Fox")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_successful(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_food("Bone", 1000.0)
        result = my_pet_shop.feed_pet("Bone", "Rex")
        self.assertEqual("Rex was successfully fed", result)
        self.assertEqual({"Bone": 900.0}, my_pet_shop.food)

    def test_feed_pet_adding_food(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_food("Bone", 2.0)
        result = my_pet_shop.feed_pet("Bone", "Rex")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"Bone": 1002.0}, my_pet_shop.food)

    def test_feed_pet_no_food(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_food("Bone", 1000.0)
        result = my_pet_shop.feed_pet("Meat", "Rex")
        self.assertEqual("You do not have Meat", result)

    def test_repr(self):
        my_pet_shop = PetShop("Sweet Pets")
        my_pet_shop.add_pet("Rex")
        my_pet_shop.add_food("Bone", 1000.0)
        result = f'Shop {my_pet_shop.name}:\n' \
               f'Pets: {", ".join(my_pet_shop.pets)}'
        self.assertEqual(result, my_pet_shop.__repr__())


if __name__ == '__main__':
    unittest.main()
