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


class IntegerListTests(unittest.TestCase):
    # test the add method if element is int
    def test_integer_list_add__if_int__expect_correct_result(self):
        int_list = IntegerList(1, 2, 3)
        element_to_add = 7
        expected = [1, 2, 3, element_to_add]
        actual = int_list.add(element_to_add)
        self.assertEqual(expected, actual, "Actual does not match expected")

    # test the add method if element is not int
    def test_integer_list_add__if_not_int__expect_exception(self):
        int_list = IntegerList(1, 2, 3)
        element_to_add = "7"
        with self.assertRaises(ValueError):
            int_list.add(element_to_add)

    # We can also test the add method if element is float
    # def test_integer_list_add__if_float__expect_exception(self):
    #     int_list = IntegerList(1, 2, 3)
    #     element_to_add = 7.5
    #     with self.assertRaises(ValueError):
    #         int_list.add(element_to_add)

    # test the remove_index method if index in range
    def test_integer_list_remove_index__if_in_range__to_return_removed_element(self):
        int_list = IntegerList(1, 2, 3)
        index_to_remove = 0
        expected = 1
        actual = int_list.remove_index(index_to_remove)
        self.assertEqual(expected, actual)

    # test the remove_index method if index out of range
    def test_integer_list_remove_index__if_not_in_range__expect_exception(self):
        int_list = IntegerList(1, 2, 3)
        index_to_remove = 5
        with self.assertRaises(IndexError):
            int_list.remove_index(index_to_remove)

    # test get method if index in range
    def test_integer_list_get__if_index_in_range__to_return_element(self):
        int_list = IntegerList(1, 2, 3)
        index = 1
        expected = 2
        actual = int_list.get(index)
        self.assertEqual(expected, actual)

    # test get method if index out in range
    def test_integer_list_get__if_index_not_in_range__expect_exception(self):
        int_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            int_list.get(index)

    # test insert method if index in range and element is int
    def test_integer_list_insert__if_index_in_range_and_el_is_int__expect_correct_result(self):
        int_list = IntegerList(1, 2, 3)
        index_to_insert = 1
        element_to_insert = 7
        int_list.insert(index_to_insert, element_to_insert)
        expected = [1, element_to_insert, 2, 3]
        actual = int_list.get_data()
        self.assertEqual(expected, actual)

    # test insert method if index not in range
    def test_integer_list_insert__if_index_not_in_range__expect_exception(self):
        int_list = IntegerList(1, 2, 3)
        index_to_insert = 4
        element_to_insert = 7
        with self.assertRaises(IndexError):
            int_list.insert(index_to_insert, element_to_insert)

    # test insert method if element is not int
    def test_integer_list_insert__if_element_not_int__expect_exception(self):
        int_list = IntegerList(1, 2, 3)
        index_to_insert = 2
        element_to_insert = "7"
        with self.assertRaises(ValueError):
            int_list.insert(index_to_insert, element_to_insert)

    # test get_biggest method
    def test_integer_list_get_biggest__to_return_biggest_number(self):
        int_list = IntegerList(1, 2, 3)
        biggest_num = 3
        self.assertEqual(biggest_num, int_list.get_biggest())

    # test get_index method
    def test_integer_list_get_index__to_return_correct_index(self):
        int_list = IntegerList(1, 2, 3)
        element = 3
        element_index = 2
        self.assertEqual(element_index, int_list.get_index(element))


if __name__ == "__main__":
    unittest.main()