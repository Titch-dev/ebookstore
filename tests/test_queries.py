from unittest import TestCase
import sqlite3

from account import Account
from data.db_build import CREATE_BOOK_TABLE, INSERT_BOOK_VALUES, INITIAL_BOOK_VALUES, CREATE_ACCOUNT_TABLE, \
    INITIAL_ACC_VALUES, INSERT_ACC_VALUES, CREATE_BASKET_TABLE, INITIAL_BASKET_VALUES, INSERT_BASKET_VALUES
from data.db_query import return_books_by_author, return_all_books, insert_book, return_books_by_id, delete_book_by_id, \
    return_books_by_title, replace_book, delete_account_by_username, \
    insert_account, return_books_from_basket, insert_basket, \
    delete_basket_record, deduct_book_quantity, update_account_address, return_account_by_username, \
    return_accounts_by_type, update_account, return_accounts_by_username, return_accounts_by_id
from book import Book
from env.database_context import DATABASE


class TestQueries(TestCase):

    def setUp(self) -> None:
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS book")
        self.cursor.execute(CREATE_BOOK_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS account")
        self.cursor.execute(CREATE_ACCOUNT_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS basket")
        self.cursor.execute(CREATE_BASKET_TABLE)
        self.cursor.executemany(INSERT_BOOK_VALUES, INITIAL_BOOK_VALUES)
        self.cursor.executemany(INSERT_ACC_VALUES, INITIAL_ACC_VALUES)
        self.cursor.executemany(INSERT_BASKET_VALUES, INITIAL_BASKET_VALUES)
        self.conn.commit()

    def tearDown(self) -> None:
        self.cursor.close()
        self.conn.close()

    ### Test Account queries ###
    def test_return_account_by_username(self):
        username = 'admin1'

        expected = (1, 'admin1', 'Pa$$word1', 'admin', None)
        actual = return_account_by_username(username)

        self.assertEqual(expected, actual)

    def test_return_accounts_by_username(self):
        username = 'adm'

        expected = [(1, 'admin1', 'Pa$$word1', 'admin', None)]
        actual = return_accounts_by_username(username)

        self.assertEqual(expected, actual)

    def test_return_accounts_by_id(self):
        _id = 2

        expected = [(2, 'customer1', 'Pa$$word1', 'customer', None)]
        actual = return_accounts_by_id(_id)

        self.assertEqual(expected, actual)

    def test_return_accounts_by_type(self):
        _type = 'customer'

        expected_cust = [(2, 'customer1', 'Pa$$word1', 'customer', None)]
        actual_cust = return_accounts_by_type(_type)

        self.assertEqual(expected_cust, actual_cust)

    def test_insert_account(self):
        admin_acc = Account.create('TestAdmin', 'Test', 'admin')
        admin = admin_acc.json()
        insert_account(admin)

        expected_admin = (3, 'TestAdmin', 'Test', 'admin', None)
        actual_admin = return_account_by_username(admin['username'])

        cust_acc = Account.create('TestCust', 'Test', 'customer')
        cust = cust_acc.json()
        insert_account(cust)

        expected_cust = (4, 'TestCust', 'Test', 'customer', None)
        actual_cust = return_account_by_username(cust['username'])

        self.assertEqual(expected_admin, actual_admin)
        self.assertEqual(expected_cust, actual_cust)

    def test_update_account(self):
        acc = Account(1,'admin1', 'test', 'admin', None)
        acc_json = acc.json()
        update_account(acc_json)

        expected = (1,'admin1', 'test', 'admin', None)
        actual = return_account_by_username(acc_json['username'])

        self.assertEqual(expected, actual)

    def test_update_account_address(self):
        username = 'admin1'
        address = 'Test New Address'
        update_account_address(username, address)

        expected = (1, 'admin1', 'Pa$$word1', 'admin', 'Test New Address')
        actual = return_account_by_username(username)

        self.assertEqual(expected, actual)

    def test_delete_account_by_username(self):
        username = 'admin1'
        delete_account_by_username(username)

        deleted = (1, 'admin1', 'Pa$$word1', 'admin', 'N/A')
        actual = return_account_by_username(username)

        self.assertNotEqual(deleted, actual)

    ### Test Book queries ###
    def test_return_all_books(self):
        expected = [
            (3001, 'A Tale of Two Cities', 'Charles Dickens', 30, 200),
            (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40, 180),
            (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25, 270),
            (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37, 325),
            (3005, 'Alice in Wonderland', 'Lewis Carroll', 12, 175)
        ]
        actual = return_all_books()

        self.assertListEqual(expected, actual)

    def test_return_books_by_id(self):
        _id = 3001
        expected = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30, 200)]
        actual = return_books_by_id(_id)

        self.assertEqual(expected, actual)

    def test_return_books_by_title(self):
        title = 'A Tale'

        expected = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30, 200)]
        actual = return_books_by_title(title)

        self.assertEqual(expected, actual)

    def test_return_books_by_author(self):
        author = 'Rowling'

        expected = [(3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40, 180)]
        actual = return_books_by_author(author)

        self.assertListEqual(expected, actual)

    def test_update_book(self):
        updated_book = Book(3002, 'Updated title', 'Updated author', 1, 100).json()
        replace_book(updated_book)

        expected = [(3002, 'Updated title', 'Updated author', 1, 100)]
        actual = return_books_by_id(3002)

        self.assertEqual(expected, actual)

    def test_insert_book(self):
        b = Book.create('Test Title', 'Test Author', 1, 100).json()
        insert_book(b)

        expected = [(3006, 'Test Title', 'Test Author', 1, 100)]
        actual = return_books_by_id(3006)

        self.assertEqual(expected, actual)

    def test_delete_book_by_id(self):
        _id = 3005
        deleted = [(3005, 'Alice in Wonderland', 'Lewis Carroll', 12, 175)]
        delete_book_by_id(_id)
        actual = return_books_by_id(_id)

        self.assertNotEqual(deleted, actual)

    def test_deduct_book_quantity(self):
        # (3001, 'A Tale of Two Cities', 'Charles Dickens', 30, 200)
        book_id = 3001
        deduction = 5
        deduct_book_quantity(book_id, deduction)

        expected = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 25, 200)]
        actual = return_books_by_id(book_id)

        self.assertEqual(expected, actual)


    ### Test Basket queries ###
    def test_return_books_from_basket(self):
        customer_id = 2
        expected = [(3001, 2), (3004, 1)]
        actual = return_books_from_basket(customer_id)

        self.assertEqual(expected, actual)

    def test_insert_basket(self):
        cust_id = 2
        book_id = 3002
        quantity = 1
        insert_basket(cust_id, book_id, quantity)

        expected = [(3001, 2), (3002, 1), (3004, 1)]
        actual = return_books_from_basket(cust_id)

        self.assertEqual(expected, actual)

    def test_delete_basket_record(self):
        cust_id = 2
        book_id = 3001
        delete_basket_record(cust_id, book_id)

        expected = [(3004, 1)]
        actual = return_books_from_basket(cust_id)

        self.assertEqual(expected, actual)
