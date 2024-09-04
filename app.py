# Utilities
from utilities.account_utils import account_search, delete_account, update_user_account, login, create_account
from utilities.basket_utils import add_book_to_basket, view_basket
from utilities.book_utils import create_book, book_search, update_book, delete_book
from utilities.general_utils import display_formatter, return_to_menu
# Templates
import templates.templates as t


def admin_management(account: dict):
    """Function that provides admin a number of options for admins
    to perform administrative responsibilities

    Parameters:
        account: Dictionary of account
    """
    while account:
        user_option = input(t.ADMIN_MANAGE_MENU)

        if user_option == '1':  # Search account
            account_search()
            continue

        elif user_option == '2':  # Create admin account
            print(t.ADD_ADMIN_ACCOUNT)
            create_account('admin')
            continue

        elif user_option == '3':  # Delete account
            account = account_search()

            if account:
                delete_account(account)

            else:
                continue

        elif user_option == '4':  # Update account
            update_user_account(account)
            continue

        else:
            break  # Return to main menu


##### Application Start #####
user_acc = None

while not user_acc:
    user_choice = input(t.WELCOME_MENU)

    if user_choice == '1':
        user_acc = login()
    elif user_choice == '2':  # Register a new user
        create_account('customer')
    else:
        print(display_formatter(t.ERROR_MESSAGE, 'Please enter a valid number'))

while user_acc['acc_type'] == 'admin':

    menu_choice = input(t.ADMIN_MENU)

    if menu_choice == '1':  # Enter book
        create_book()  #
        return_to_menu()

    elif menu_choice == '2':  # Update book
        book = book_search()  # Returns a dictionary
        if book:
            update_book(book)
        else:
            continue  # Returns to menu

    elif menu_choice == '3':  # Delete book
        book = book_search()
        if book:
            delete_book(book)
        else:
            continue  # Returns to menu

    elif menu_choice == '4':  # Search books
        book_search()
        return_to_menu()

    elif menu_choice == '5':  # Admin Management
        admin_management(user_acc)

    elif menu_choice == '0':
        print(display_formatter(t.LOGOUT, user_acc['username']))
        break

    else:
        print(display_formatter(t.ERROR_MESSAGE, 'Not a valid menu option'))
        return_to_menu()

while user_acc['acc_type'] == 'customer':

    menu_choice = input(t.CUSTOMER_MENU)

    if menu_choice == '1':  # Search book
        book = book_search()
        if book:
            add_book_to_basket(book, user_acc['id'])
        else:
            continue

    elif menu_choice == '2':  # View basket
        view_basket(user_acc)

    elif menu_choice == '3':  # Manage account
        update_user_account(user_acc)

    elif menu_choice == '0':  # Logout
        print(display_formatter(t.LOGOUT, user_acc['username']))
        break

    else:
        input(display_formatter(t.ERROR_MESSAGE, 'Not a valid menu option'))

user_acc = None  # Ensure that user session is terminated
