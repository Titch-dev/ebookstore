# Utilities
from utilities.book_utils import book_mapping, print_book
from utilities.general_utils import enumerate_object, display_formatter, return_to_menu
# Templates
import templates.templates as t
# DB Queries
from data.db_query import return_books_from_basket, return_books_by_id, insert_basket, delete_basket_record, \
    deduct_book_quantity, update_account_address


def print_basket(enumerated_books: dict):
    """Function to cycle through basket, print books and tally cost

    Parameters:
        enumerated_books: Dictionary of books
    """
    total_price = 0
    for position, book in enumerated_books.items():
        print_book(book, position)
        total_price += book['price'] * book['quantity']

    print(display_formatter(t.CUSTOMER_BASKET_VALUE, total_price))


def update_basket(book: dict, user_acc: dict):
    """Function to update basket according to user inputs

    Parameters:
        book: Dictionary of a book
        user_acc: Dictionary of user account
    """
    user_choice = input(t.UPDATE_BASKET)

    if user_choice == '1':  # Update quantity1

        while True:
            try:
                new_quantity = int(input('NEW AMOUNT: '))
                data = return_books_by_id(book['id'])
                inventory_book = book_mapping(data)

                if new_quantity < inventory_book['quantity']:
                    insert_basket(user_acc['id'], book['id'], new_quantity)
                    print(display_formatter(t.CONFIRM_MESSAGE, f'{new_quantity} * \'{book['title']}\''
                                                               f'\nhas been added to your basket'))

                elif new_quantity == 0:
                    delete_basket_record(user_acc['id'], book['id'])
                    print(display_formatter(t.CONFIRM_MESSAGE, f'{book['title']} removed from basket'))
                    break

                else:
                    print(display_formatter(t.ERROR_MESSAGE, f'We don\'t have enough. '
                                                             f'We have {inventory_book['quantity']} left'))
                    continue

            except ValueError:
                print(display_formatter(t.ERROR_MESSAGE, "Please enter a number"))
                continue

    elif user_choice == '2':  # Remove from basket
        delete_basket_record(user_acc['id'], book['id'])
        print(display_formatter(t.CONFIRM_MESSAGE, f'\'{book['title']}\' has '
                                                   f'been removed from your basket'))

    else:  # exit to menu
        return_to_menu()


def checkout(book_basket: dict, user_acc: dict):
    """Function to check whether user account has an address and
        call update address if not. Remove the

    Parameters:
        book_basket: dictionary of books
        user_acc: dictionary of account
    """
    if not user_acc['address']:
        while True:
            print(display_formatter(t.CONFIRM_MESSAGE, 'Please provide an address to deliver to'))
            address = input('ADDRESS: ')
            user_acc['address'] = address
            print(display_formatter(t.ACC_PROFILE,
                                    user_acc['username'],
                                    user_acc['password'],
                                    user_acc['acc_type'],
                                    user_acc['address']))
            user_choice = input(t.CONFIRM_ACC_UPDATE)
            if user_choice == '1':  # Confirm address
                update_account_address(user_acc['username'], address)
                break  # Continue to checkout
            else:
                print(display_formatter(t.ERROR_MESSAGE, 'Without an address, we cannot deliver!'))
                continue  # Repeat address

    purchase_option = input(t.CONFIRM_PURCHASE)

    if purchase_option == '1':
        for book in book_basket.values():  # Remove basket from database, deduct book quantities
            deduct_book_quantity(book['id'], book['quantity'])
            delete_basket_record(user_acc['id'], book['id'])

        print(display_formatter(t.CONFIRM_MESSAGE, f'Thanks {user_acc['username']} for your purchase,'
                                                   f'\nwe hope you enjoy your new books'))


def add_book_to_basket(book: dict, user_id: int):
    """Function to update user basket

    Parameters:
        book: Dictionary of book
        user_id: ID integer of user
    """
    user_option = input(t.CUSTOMER_ADD)

    if user_option == '1':  # Add book to basket
        while True:
            try:
                quantity = int(input('Please enter the number of copies you would like: '))
                if book['quantity'] <= quantity:
                    print(display_formatter(t.ERROR_MESSAGE, f'Unfortunately we don\'t have enough copies '
                                                             f'for you :( \n\t There\'s {book['quantity']} left'))
                    continue
                else:
                    insert_basket(user_id, book['id'], quantity)
                    print(display_formatter(t.CONFIRM_MESSAGE, f'{quantity} * {book['title']}'
                                                               f'\n\thave been added to your basket'))
                    break
            except ValueError:
                print(display_formatter(t.ERROR_MESSAGE, 'Please enter a valid number'))


def basket_option(basket: dict, user_acc: dict):
    """Function to action basket features

    Parameters:
        basket: Enumerated Dictionary
        user_acc: Dictionary of user account
    """
    checkout_option = len(basket.keys()) + 1  # The integer assigned to check out

    try:
        basket_choice = int(input(display_formatter(t.CUSTOMER_BASKET_OPTION, checkout_option)))

        if basket_choice in basket.keys():  # If an int is input that corresponds to basket
            book = basket[basket_choice]
            print_book(book)
            update_basket(book, user_acc)

        elif basket_choice == checkout_option:
            checkout(basket, user_acc)

    except ValueError:
        return_to_menu()


def retrieve_basket(user_id: int) -> dict:
    """Function to return a list of Book jsons equal to
    customer basket an empty list

    Parameters:
        user_id: Current user id

    Returns:
        enumerated dictionary
    """
    book_ids = return_books_from_basket(user_id)
    book_basket = []

    # If there are any books in basket add to basket list
    if book_ids:
        for _id, quantity in book_ids:
            data = return_books_by_id(_id)
            book_json = book_mapping(data)
            book_json['quantity'] = quantity  # Update the 'quantity' value to user basket quantity
            book_basket.append(book_json)

        enumerated_books = enumerate_object(book_basket)
        print_basket(enumerated_books)

        return enumerated_books


def view_basket(user_acc: dict):
    """Function to return user basket or display empty

    Parameters:
        user_acc: Dictionary of user account
    """
    print(t.CUSTOMER_BASKET_HEADING)
    basket = retrieve_basket(user_acc['id'])

    if basket:
        print_basket(basket)
        basket_option(basket, user_acc)
    else:
        input(t.CUSTOMER_BASKET_EMPTY)
