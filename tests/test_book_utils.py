from unittest import TestCase

from book import Book
from utilities.book_utils import book_mapping
from utilities.general_utils import display_formatter
import templates.templates as t


class TestBookUtils(TestCase):

    def test_book_mapping(self):
        book = (1, 'Test1', 'Test author1', 10, 100)
        list_1 = [(1, 'Test1', 'Test author1', 10, 100)]
        list_multi = [(1, 'Test1', 'Test author1', 10, 100), (2, 'Test2', 'Test author2', 20, 200)]

        expected_dict = {'id': 1, 'title': 'Test1', 'author': 'Test author1', 'quantity': 10, 'price': 100}
        expected_list = [{'id': 1, 'title': 'Test1', 'author': 'Test author1', 'quantity': 10, 'price': 100},
                         {'id': 2, 'title': 'Test2', 'author': 'Test author2', 'quantity': 20, 'price': 200}]

        actual_book = book_mapping(book)
        actual_list_1 = book_mapping(list_1)
        actual_list_multi = book_mapping(list_multi)

        self.assertEqual(expected_dict, actual_book)
        self.assertEqual(expected_dict, actual_list_1)
        self.assertEqual(expected_list, actual_list_multi)

    def test_create_book(self):
        pass

    def test_update_field(self):
        pass

    def test_update_book(self):
        pass

    def test_delete_book(self):
        pass

    def test_refine_author(self):
        pass

    def test_refine_book_search(self):
        pass

    def test_search_book(self):
        pass