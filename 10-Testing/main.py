import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)

    def test_lower(self):
        result = "TOO".lower()
        expected_result = "too"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

