# RS 100/100 in judge:
import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class TestIntegerList(unittest.TestCase):
    # def test_init_constructor_without_data(self):
    #     test_int = IntegerList()  # test if a blank list can be instantiated
    #     self.assertEqual([], test_int._IntegerList__data)

    # def test_init_constructor_with_wrong_data(self):
    #     test_int = IntegerList("asd", 5.2, True)  # test if a blank list can be instantiated
    #     self.assertEqual([], test_int._IntegerList__data)

    def test_init_constructor_with_correct_data(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)  # test if a blank list can be instantiated
        self.assertEqual([1, 2, 3, 4], test_int.get_data())

    def test_get_data(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        result = test_int.get_data()
        self.assertEqual([1, 2, 3, 4], result)

    def test_add_raises_ValueError(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        with self.assertRaises(ValueError) as ex:
            test_int.add("asd")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_with_correct_data(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        result = test_int.add(5)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_remove_index_raises_IndexError(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        with self.assertRaises(IndexError) as ex:
            test_int.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_correct(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        result = test_int.remove_index(0)
        self.assertEqual(1, result)

    def test_get_invalid_index_raise_IndexError(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        with self.assertRaises(IndexError) as ex:
            test_int.get(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        result = test_int.get(0)
        self.assertEqual(1, result)

    def test_insert_invalid_index_raises_IndexError(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        with self.assertRaises(IndexError) as ex:
            test_int.insert(4, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        test_int.insert(3, 5)
        self.assertEqual([1, 2, 3, 5, 4], test_int.get_data())

    def test_insert_invalid_integer_raises_ValueError(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        with self.assertRaises(ValueError) as ex:
            test_int.insert(3, "5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        result = test_int.get_biggest()
        self.assertEqual(4, result)

    def test_get_index(self):
        test_int = IntegerList("asd", 1, 2, 3, 4)
        test_int.get_index(1)
        self.assertEqual(0, test_int.get_index(1))


if __name__ == "__main__":
    unittest.main()
