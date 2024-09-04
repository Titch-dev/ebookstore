from unittest import TestCase
from book import Book


class TestBook(TestCase):
    def test_create(self):
        expected = Book('-', 'Test', 'Test1', 10, 100).json()
        actual = Book.create('Test', 'Test1', 10, 100).json()

        self.assertEqual(expected, actual)

    def test_json(self):
        expected = {'id': 1, 'title': 'Test1', 'author': 'Test author1', 'quantity': 10, 'price': 100}
        actual = Book(1, 'Test1', 'Test author1', 10, 100).json()

        self.assertEqual(expected, actual)