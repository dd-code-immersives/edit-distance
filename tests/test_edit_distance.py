import unittest
import csv
from edit_distance import edit_distance


class EditDistanceTests(unittest.TestCase):
    """
    Edit distance unit tests
    """

    def test_edit_distance_simple_examples(self):
        """
        basic examples for edit distance
        """
        self.assertEqual(edit_distance("the", "the"), 0)
        self.assertEqual(edit_distance("hen", "ben"), 1)
        self.assertEqual(edit_distance("the", "then"), 1)
        self.assertEqual(edit_distance("then", "the"), 1)
        self.assertEqual(edit_distance("the", "again"), 5)

    def test_edit_distance_bulk(self):
        """
        randomly generated examples for edit distance
        """
        with open('data/wordlist.csv') as csvfile:
            examples = csv.reader(csvfile)
            for row in examples:
                self.assertEqual(edit_distance(row[0], row[1]), int(row[2]))


if __name__ == '__main__':
    unittest.main()
