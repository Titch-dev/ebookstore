import sqlite3

# Uncomment to build either production or test databases
db = sqlite3.connect('ebookstore.db')  # Production database
# db = sqlite3.connect('ebookstore_test.db')  # Test database

cur = db.cursor()

CREATE_ACCOUNT_TABLE = '''
CREATE TABLE IF NOT EXISTS account(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(20) NOT NULL,
    acc_type VARCHAR(10) NOT NULL,
    address VARCHAR(200) DEFAULT NULL
)
'''

INSERT_ACC_VALUES = '''
INSERT or REPLACE INTO account (id, username, password, acc_type)
    VALUES (?,?,?,?)
'''

INITIAL_ACC_VALUES = [
    (1, 'admin1', 'Pa$$word1', 'admin'),
    (2, 'customer1', 'Pa$$word1', 'customer')
]

CREATE_BOOK_TABLE = '''
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    qty INT DEFAULT 0,
    price FLOAT NOT NULL
)
'''

INSERT_BOOK_VALUES = '''
INSERT or REPLACE INTO book
    VALUES (?, ?, ?, ?, ?)
'''

INITIAL_BOOK_VALUES = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30, 200),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40, 180),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25, 270),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37, 325),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12, 175)
]

CREATE_BASKET_TABLE = '''
CREATE TABLE IF NOT EXISTS basket(
    customer_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    CONSTRAINT fk_account
        FOREIGN KEY(customer_id) 
        REFERENCES account(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_book
        FOREIGN KEY(book_id) 
        REFERENCES book(id)
        ON DELETE CASCADE,
    PRIMARY KEY(customer_id, book_id)
)
'''

INSERT_BASKET_VALUES = '''
INSERT or REPLACE INTO basket
    VALUES (?,?,?)
'''

INITIAL_BASKET_VALUES = [(2, 3001, 2),
                         (2, 3004, 1)]


try:
    cur.execute('DROP TABLE IF EXISTS book')  # Delete 'book' table from database
    cur.execute(CREATE_BOOK_TABLE)  # Create 'book' table
    cur.execute('DROP TABLE IF EXISTS account')  # Delete 'account' table from database
    cur.execute(CREATE_ACCOUNT_TABLE)  # Create 'account' table
    cur.execute('DROP TABLE IF EXISTS basket')  # Delete 'basket' table from database
    cur.execute(CREATE_BASKET_TABLE)  # Create 'basket' table
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

try:
    cur.executemany(INSERT_BOOK_VALUES, INITIAL_BOOK_VALUES)  # Insert book values into book table
    cur.executemany(INSERT_ACC_VALUES, INITIAL_ACC_VALUES)  # Insert account values into book table
    cur.executemany(INSERT_BASKET_VALUES, INITIAL_BASKET_VALUES)  # Insert basket values into basket
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

db.close()
