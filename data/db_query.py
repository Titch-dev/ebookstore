import sqlite3

from env.database_context import DATABASE


def database_connection() -> tuple:
    """Function to make connection to database"""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    return connection, cursor


### Account queries ###
def return_account_by_username(username: str) -> tuple:
    """Function to query database and return account record by username

    Parameters:
        username: String of account username

    Returns:
        Tuple of account
        """
    con, cur = database_connection()
    command = 'SELECT * FROM account WHERE username = ?'
    cur.execute(command, (username,))
    data = cur.fetchone()
    con.close()
    return data


def return_accounts_by_username(username: str) -> list[tuple]:
    """Function to query database and return a list of accounts
    by username

    Parameters:
        username: String of account username

    Returns:
        A list of account tuples
    """
    con, cur = database_connection()
    username = f'%{username}%'
    command = 'SELECT * FROM account WHERE username LIKE ?'
    cur.execute(command, (username,))
    data = cur.fetchall()
    con.close()

    return data


def return_accounts_by_id(_id: int) -> list[tuple]:
    """Function to query database and return a list of accounts

    Parameters:
        _id: Account id integer

    Returns:
        A list of account tuples
    """
    con, cur = database_connection()
    _id = f'%{_id}%'
    command = f'SELECT * FROM account WHERE id LIKE ? GROUP BY acc_type'
    cur.execute(command, (_id,))
    data = cur.fetchall()
    con.close()

    return data


def return_accounts_by_type(acc_type: str) -> list[tuple]:
    """Function to query database and return a list of accounts
    by type

    Parameters:
        acc_type: String of account type

    Returns:
        A list of account tuples
    """
    con, cur = database_connection()
    command = 'SELECT * FROM account WHERE acc_type = ?'
    cur.execute(command, (acc_type,))
    data = cur.fetchall()
    con.close()

    return data


def insert_account(account: dict):
    """Function to insert account

    Parameters:
        account: A dictionary of an account
    """
    con, cur = database_connection()
    command = 'INSERT INTO account (username, password, acc_type) VALUES (?,?,?)'
    cur.execute(command, (account['username'],
                          account['password'],
                          account['acc_type']))
    con.commit()
    con.close()


def update_account(account: dict):
    """Function to update account information

    Parameters:
        account: A dictionary of an account
    """
    con, cur = database_connection()
    command = 'INSERT OR REPLACE INTO account VALUES(?,?,?,?,?)'
    cur.execute(command, (account['id'],
                          account['username'],
                          account['password'],
                          account['acc_type'],
                          account['address'])
                )
    con.commit()
    con.close()


def update_account_address(username: str, address: str):
    """Function to update address of an account

    Parameters:
        username: A string of an account username
        address: A string of an account address
    """
    con, cur = database_connection()
    command = 'UPDATE account SET address = ? WHERE username = ?'
    cur.execute(command, (address, username))
    con.commit()
    con.close()


def delete_account_by_username(username: str):
    """Function to delete an account record

    Parameters:
        username: A string of an account username
    """
    con, cur = database_connection()
    command = 'DELETE FROM account WHERE username = ?'
    cur.execute(command, (username,))
    con.commit()
    con.close()


### Book queries ###
def return_all_books() -> list[tuple]:
    """Function to query database and return all book records

    Returns:
        A list of book tuples
    """
    con, cur = database_connection()
    command = 'SELECT * FROM book'
    cur.execute(command)
    data = cur.fetchall()
    con.close()
    return data


def return_books_by_id(_id: int) -> list[tuple]:
    """Function to query database and return all books that match on id

    Parameters:
        _id: Book id integer

    Returns:
        A list of book tuples
    """
    con, cur = database_connection()
    _id = f'%{_id}%'
    command = 'SELECT * FROM book WHERE id LIKE ?'
    cur.execute(command, (_id,))
    data = cur.fetchall()
    con.close()
    return data


def return_books_by_title(title: str) -> list[tuple]:
    """Function to query database and return all books matched on title

    Parameters:
        title: String of a book title

    Returns:
        A list of book tuples
    """
    con, cur = database_connection()
    title = f'%{title}%'
    command = 'SELECT * FROM book WHERE title LIKE ?'
    cur.execute(command, (title,))
    data = cur.fetchall()
    con.close()
    return data


def return_books_by_author(author: str) -> list[tuple]:
    """Function to query database and return all books matched on author

    Parameters:
        author: String of book author

    Returns:
        A list of book tuples
    """
    con, cur = database_connection()
    author = f'%{author}%'
    command = 'SELECT * FROM book WHERE author LIKE ?'
    cur.execute(command, (author,))
    data = cur.fetchall()
    con.close()
    return data


def replace_book(book: dict):
    """Function to replace book record in database with user defined book

    Parameters:
        book: Dictionary of a book
    """
    con, cur = database_connection()
    command = 'INSERT OR REPLACE INTO book(id, title, author, qty, price) VALUES (?,?,?,?,?)'
    cur.execute(command, (book['id'],
                          book['title'],
                          book['author'],
                          book['quantity'],
                          book['price']))
    con.commit()
    con.close()


def insert_book(book: dict):
    """Function to insert a book record into database

    Parameters:
        book: Dictionary of a book
    """
    con, cur = database_connection()
    command = "INSERT INTO book (title, author, qty, price) VALUES (?,?,?,?)"
    cur.execute(command, (book['title'],
                          book['author'],
                          book['quantity'],
                          book['price']))
    con.commit()
    con.close()


def delete_book_by_id(_id: int):
    """Function to delete book record in database on book id

    Parameters:
        _id: Integer of book id
    """
    con, cur = database_connection()
    command = "DELETE FROM book WHERE id = ?"
    cur.execute(command, (_id,))
    con.commit()
    con.close()


def deduct_book_quantity(book_id: int, deduction: int):
    """Function to deduct quantity from book

    Parameters:
        book_id: Integer of book id
        deduction: Integer of amount to deduct from DB
    """
    con, cur = database_connection()
    command = 'UPDATE book SET qty = (qty - ?) WHERE id = ?'
    cur.execute(command, (deduction, book_id))
    con.commit()
    con.close()


##### Basket queries #####
def return_books_from_basket(customer_id: int):
    """Function to return customer basket

    Parameters:
        customer_id: Integer of customer id
    """
    con, cur = database_connection()
    command = "SELECT book_id, quantity FROM basket WHERE customer_id = ?"
    cur.execute(command, (customer_id,))
    data = cur.fetchall()
    con.close()
    return data


def insert_basket(customer_id: int, book_id: int, quantity: int):
    """Function to add book to customer's basket

    Parameters:
        customer_id: Integer of account id
        book_id: Integer of book id
        quantity: Integer of amount of books to insert
    """
    con, cur = database_connection()
    command = "INSERT OR REPLACE INTO basket VALUES (?,?,?)"
    cur.execute(command, (customer_id, book_id, quantity))
    con.commit()
    con.close()


def delete_basket_record(customer_id: int, book_id: int):
    """Function to remove book from basket

    Parameters:
        customer_id: Integer of account id
        book_id: Integer of book id
    """
    con, cur = database_connection()
    command = "DELETE FROM basket WHERE customer_id = (?) AND book_id = (?)"
    cur.execute(command, (customer_id, book_id))
    con.commit()
    con.close()
