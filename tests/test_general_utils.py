from book import Book

from utilities.general_utils import display_formatter, enumerate_object, password_validator
from unittest import TestCase

# Templates
import templates.templates as t


class TestGeneralUtils(TestCase):

    def test_password_validator(self):
        passed = 'Pa$$word1'
        actual = password_validator(passed)
        self.assertTrue(actual)

        not_passed = 'password'
        actual = password_validator(not_passed)
        self.assertFalse(actual)

    def test_display_formatter(self):
        expected_display = '''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * *

        Test, you have successfully
                logged out, Good Bye!!!

* * * * * * * * * * * * * * * * * * * * * * * * * * * * *'''
        actual_display = display_formatter(t.LOGOUT, 'Test')
        self.assertEqual(expected_display, actual_display)

    def test_enumerate_object(self):

        objects = [{'test': 100}, {'test': 200}]
        actual = enumerate_object(objects)
        expected = {1: {'test': 100},
                    2: {'test': 200}}

        self.assertEqual(expected, actual)




