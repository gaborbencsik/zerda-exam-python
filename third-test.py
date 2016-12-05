from third import count_letter_in_string
import unittest

class TestCountLetter(unittest.TestCase):

    def test_real_string(self):
        self.assertEqual(count_letter_in_string("appletree", "e"), 3)

    def test_not_letter(self):
        self.assertEqual(count_letter_in_string("appletree", 1), 0)

    def test_not_string(self):
        self.assertEqual(count_letter_in_string(123, "a"), 0)

    def test_both_int(self):
        self.assertEqual(count_letter_in_string(1232, 2), 0)

    def test_letter_as_list(self):
        self.assertRaises(TypeError, count_letter_in_string, ("appletree", ["a","e"]))




if __name__ == '__main__':
    unittest.main()
