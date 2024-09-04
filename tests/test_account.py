from unittest import TestCase
from account import Account

class TestAccount(TestCase):
    def test_create(self):
        expected = Account('-', 'Test', 'Test1', 'admin', None).json()
        actual = Account.create('Test', 'Test1', 'admin').json()

        self.assertEqual(expected, actual)

    def test_json(self):
        expected = {'id': 1, 'username': 'Test', 'password': 'Test1', 'acc_type': 'admin', 'address': None}
        actual = Account(1, 'Test', 'Test1', 'admin', None).json()

        self.assertEqual(expected, actual)




