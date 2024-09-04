# Objects
from book import Book
# Utility functions
from utilities.general_utils import display_formatter, enumerate_object, return_to_menu
# Templates
import templates.templates as t
# DB Queries
from data.db_query import replace_book, insert_book, return_all_books, return_books_by_author, return_books_by_title, \
    return_books_by_id, delete_book_by_id


def print_book(book: dict, position: int = None):
    """Function print a book conditionally on whether a 'position' is provided

    Parameters:
        book: Dictionary of a book
        position: Integer of position
    """
    if position:
        print(display_formatter(t.ENUMERATED_BOOK,
                                position,
                                book['id'],
                                book['title'],
                                book['author'],
                                book['quantity'],
                                book['price'])
              )

    else:
        print(display_formatter(t.BOOK,
                                book['id'],
                                book['title'],
                                book['author'],
                                book['quantity'],
                                book['price'])
              )


def book_mapping(data: list[tuple] | tuple) -> list[dict] | dict:
    """Function to parse a tuple/s and return a book/s as a
    dictionary or a list of dictionaries

    Parameter:
        data: A list of book tuples or a single tuple

    Returns:
        Either a list dictionaries or a single dictionary
    """
    if type(data) is tuple:
        book = Book(data[0], data[1], data[2], data[3], data[4]).json()
        return book

    else:  # if list of tuples
        books = list()
        for book in data:
            book = Book(book[0], book[1], book[2], book[3], book[4]).json()
            books.append(book)

        if len(books) > 1:
            return books

        else:  # returns dictionary of book if only one in 'books' list
            return books[0]


def create_book():
    """Function to take book input and insert book to the database"""
    print(display_formatter(t.CONFIRM_MESSAGE, 'Please answer the following'))

    while True:
        try:
            title = input('TITLE: ')
            author = input('AUTHOR: ')
            quantity = int(input('QUANTITY: '))
            price = int(input('PRICE: '))

            book = Book.create(title, author, quantity, price).json()
            display_formatter(t.BOOK,
                              book['id'],
                              book['title'],
                              book['author'],
                              book['quantity'],
                              book['price'])

            user_confirm = input(t.CONFIRM_ADD_BOOK)  # Display book to add

            if user_confirm == '1':  # Add created book to database
                insert_book(book)
                return print(display_formatter(t.CONFIRM_MESSAGE, f'\'{book['title']}\' has successfully been added'))
            elif user_confirm == '2':
                continue  # Restart the new user defined book
            else:
                break  # Return to main menu
        except ValueError:
            print(display_formatter(t.ERROR_MESSAGE, 'Invalid input, please start again'))


def update_field(field: str, book: dict) -> tuple[dict, bool]:
    """Function to update changes to book record in database

    Parameters:
        field: String of the column in the database
        book: Dictionary of book

    Returns:
        A tuple of updated book dict and bool to continue updating
    """
    updated_book = book.copy()  # Incase user wishes to update several fields
    continue_updating = True

    new_value = input(f"New {field.upper()}: ")

    if new_value.isdigit() and field == 'id' or field == 'quantity':
        new_value = int(new_value)

    updated_book[field] = new_value
    print_book(updated_book)

    user_choice = input(t.CONFIRM_UPDATE)
    if user_choice == '1':  # To save
        replace_book(updated_book)
        continue_updating = False
        return updated_book, continue_updating

    elif user_choice == '2':  # To update another field
        replace_book(updated_book)
        return updated_book, continue_updating

    else:
        continue_updating = False  # Return to Update menu
        return book, continue_updating


def update_book(book: dict):
    """Function to provide user choice of what to update on book

    Parameters:
        book: Dictionary of book
    """
    is_updating = True  # Boolean to track user updating

    while is_updating:
        user_choice = input(display_formatter(t.UPDATE_BOOK,
                                              book['id'],
                                              book['title'],
                                              book['author'],
                                              book['quantity'],
                                              book['price']))
        if user_choice == '1':  # Update title
            book, is_updating = update_field('title', book)

        elif user_choice == '2':  # Update author
            book, is_updating = update_field('author', book)

        elif user_choice == '3':  # Update quantity
            book, is_updating = update_field('quantity', book)

        elif user_choice == '4':  # Update price
            book, is_updating = update_field('price', book)

        else:
            is_updating = False  # return to main menu


def delete_book(book: dict):
    """Function to confirm deletion of book record from database

    Parameters:
        book: Dictionary of book
    """
    user_option = input(t.CONFIRM_DELETE)

    if user_option == '1':
        delete_book_by_id(book['id'])
        print(display_formatter(t.CONFIRM_MESSAGE, f'Book id: {book['id']} has been deleted'))

    else:
        return_to_menu()


def refine_author(author_list: list[dict]) -> str:
    """Function returns the 'author' string conditionally on
    user choices.

    Parameters:
        author_list: List of book jsons

    Returns:
        Author name as a string
    """
    # Cycle through all authors and add author name to set, to return unique author name's only
    author_set = set()
    for book in author_list:
        author_set.add(book['author'])

    if len(author_set) > 1:  # if multiple authors
        enumerated_authors = enumerate_object(list(author_set))
        for author in enumerated_authors.items():
            print(display_formatter(t.ENUMERATED_AUTHOR, author[0], author[1]))

        while True:
            try:
                user_choice = int(input(t.REFINE_AUTHOR))

                if user_choice in enumerated_authors.keys():
                    return enumerated_authors[user_choice]
                else:
                    print(display_formatter(t.ERROR_MESSAGE, 'Please enter the corresponding ref number'))
            except ValueError:
                print(display_formatter(t.ERROR_MESSAGE, 'Please enter the corresponding ref number'))
    else:
        return author_set.pop()  # Returns author string is only 1


def refine_book_search(books: list[dict] | dict) -> dict:
    """ Function to refine user search and return book in json format

    Parameters:
        books: List of book dictionaries or a singular dictionary

    Return:
        A book dictionary
    """
    if type(books) is list:
        enumerated_books = enumerate_object(books)  # Returns a dictionary enumerated dictionary's
        while True:
            for position, book_json in enumerated_books.items():
                print_book(book_json, position)
            try:
                user_choice = int(input(t.REFINE_SEARCH))
                if user_choice in enumerated_books.keys():
                    print_book(enumerated_books[user_choice])
                    book_json = enumerated_books[user_choice]
                    return book_json
                elif user_choice == 0:
                    break  # Exit out of search
                else:
                    input(display_formatter(t.ERROR_MESSAGE, 'Reference number not in the above list'))
                    continue

            except ValueError:
                input(display_formatter(t.ERROR_MESSAGE, 'Not a valid input, please enter a number'))
                continue

    else:  # if only one book
        print_book(books)
        return books


def book_search() -> dict | None:
    """Function to return a book dictionary, conditionally on user choice

    Returns:
        A dictionary of a book
    """
    while True:
        user_option = input(t.SEARCH_BOOK)

        if user_option == '1':  # Search by id
            id_input = int(input('BOOK ID: '))
            data = return_books_by_id(id_input)

            if len(data) == 0:
                print(display_formatter(t.ERROR_MESSAGE, 'No id\'s matched your search'))
                return None

            else:
                result_json = book_mapping(data)  # books - list[dict]
                return refine_book_search(result_json)  # Returns single book - dict

        elif user_option == '2':  # Search by title
            title = input('TITLE: ')
            data = return_books_by_title(title)

            if len(data) == 0:
                print(display_formatter(t.ERROR_MESSAGE, 'No title\'s matched your search'))
                return None

            else:
                result_json = book_mapping(data)
                return refine_book_search(result_json)

        elif user_option == '3':  # Search by author
            author = input('AUTHOR: ')
            data = return_books_by_author(author)

            if len(data) == 0:
                print(display_formatter(t.ERROR_MESSAGE, 'No author\'s matched your search'))

                return None

            result_json = book_mapping(data)

            if len(data) > 1:  # If multiple authors
                chosen_author = refine_author(result_json)  # Returns author string
                data = return_books_by_author(chosen_author)
                result_json = book_mapping(data)
                return refine_book_search(result_json)

            else:
                print_book(result_json)
                return result_json

        elif user_option == '4':  # Return all books
            data = return_all_books()
            result_json = book_mapping(data)
            return refine_book_search(result_json)

        else:
            return None  # return to main menu
