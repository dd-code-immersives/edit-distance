import unittest
from edit_distance import edit_distance

class EditDistanceTests(unittest.TestCase):


    def test_edit_distance(self):
        self.assertEqual(edit_distance("the", "the"),0)
        self.assertEqual(edit_distance("hen", "ben"),1)
        self.assertEqual(edit_distance("the", "then"), 1)
        self.assertEqual(edit_distance("then", "the"), 1)
        self.assertEqual(edit_distance("the", "again"), 5)

if __name__ == '__main__':
    unittest.main()
