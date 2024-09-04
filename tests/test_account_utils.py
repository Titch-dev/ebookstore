from unittest import TestCase

from utilities.account_utils import account_mapping


class TestAccountUtils(TestCase):

    def test_account_mapping(self):
        account = (1, 'Test1', 'Test1', 'admin', None)
        list_1 = [(1, 'Test1', 'Test1', 'admin', None)]
        list_multi = [(1, 'Test1', 'Test1', 'admin', None), (2, 'Test2', 'Test2', 'customer', None)]

        expected_dict = {'id': 1, 'username': 'Test1', 'password': 'Test1', 'acc_type': 'admin','address': None}
        expected_list = [{'id': 1, 'username': 'Test1', 'password': 'Test1', 'acc_type': 'admin', 'address': None},
                         {'id': 2, 'username': 'Test2', 'password': 'Test2', 'acc_type': 'customer', 'address': None}]

        actual_account = account_mapping(account)
        actual_list_1 = account_mapping(list_1)
        actual_list_multi = account_mapping(list_multi)

        self.assertEqual(expected_dict, actual_account)
        self.assertEqual(expected_dict, actual_list_1)
        self.assertEqual(expected_list, actual_list_multi)

    def test_login(self):
        pass

    def test_create_account(self):
        pass

    def test_update_user_account(self):
        pass

    def test_delete_account(self):
        pass

    def test_refine_account_search(self):
        pass

    def test_account_search(self):
        pass


