# lr4_12.10.22 unit-test
from clas import Biblioteka
import unittest

class TestBiblioteka(unittest.TestCase):
    def setUp(self):
        self.b = Biblioteka('Психология', 115)

    def test_bib(self):
        test_books = ('Психология', 115)
        self.a = self.b.books()
        self.assertEqual(self.a, test_books)

if __name__ == '__main__':
    unittest.main()
