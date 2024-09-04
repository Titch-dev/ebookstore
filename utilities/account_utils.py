# Objects
from account import Account
# Utilities
from utilities.general_utils import display_formatter, enumerate_object, password_validator
# Templates
import templates.templates as t
# DB Queries
from data.db_query import return_accounts_by_username, delete_account_by_username, \
    return_accounts_by_id, return_accounts_by_type, return_account_by_username, insert_account, update_account


def print_account(account: dict, position: int = None):
    """Function to print an account conditionally on whether a 'position' is provided

    Parameters:
        account: Dictionary of account
        position: Integer of reference position
        """
    if position:
        print(display_formatter(t.ENUMERATED_ACCOUNT,
                                position,
                                account['id'],
                                account['username'],
                                account['password'],
                                account['acc_type'],
                                account['address']))
    else:
        print(display_formatter(t.ACC_PROFILE,
                                account['username'],
                                account['password'],
                                account['acc_type'],
                                account['address']))


def account_mapping(data: list[tuple] | tuple) -> list[dict] | dict:
    """ Function to parse tuple/s and return an account/s as a
    dictionary or list of dictionaries

    Parameter:
        data: A list of account tuples or a single tuple

    Returns:
        Either a list of dictionaries or a single dictionary
    """
    if type(data) is tuple:
        account = Account(data[0], data[1], data[2], data[3], data[4]).json()
        return account

    else:   # If list of tuples
        accounts = list()
        for acc in data:
            account = Account(acc[0], acc[1], acc[2], acc[3], acc[4]).json()
            accounts.append(account)

        if len(accounts) > 1:
            return accounts

        else:  #  Returns account dictionary if only 1 in 'accounts' list
            return accounts[0]


def login() -> dict:
    """ Function to take account input, query the database, cast result to json
    and return account dictionary

    Returns:
       Dictionary of user account
    """
    while True:
        username = input('USERNAME: ')
        password = input('PASSWORD: ')
        data = return_account_by_username(username)

        if data:
            account = account_mapping(data)
            if account['password'] == password:
                return account
            else:
                input(display_formatter(t.ERROR_MESSAGE, 'The password does not match, please try again'))
                break
        else:
            input(display_formatter(t.ERROR_MESSAGE, 'Account does not exist, please register or try again'))
            break


def create_account(acc_type: str):
    """Function to create a new account record to database

    Parameters:
        acc_type: A string referencing type of account to create"""
    is_creating = True

    while is_creating:
        username = input('USERNAME: ')
        existing_acc = return_account_by_username(username)

        if existing_acc:
            print(display_formatter(t.ERROR_MESSAGE, 'Username already exists, please try again'))

        while not existing_acc:
            password = input('PASSWORD: ')
            validated_password = password_validator(password)

            if validated_password:
                new_account = Account.create(username, password, acc_type).json()  # Create Account object

                insert_account(new_account)
                print(display_formatter(t.CONFIRM_MESSAGE, f'Thanks for registering {username}'))
                is_creating = False  # Break out of create account loop

                break

            else:
                print(t.PASSWORD_VAL_ERROR)


def update_user_account(account: dict):
    """Function to update user's account conditionally

    Parameters:
        account: Dictionary of user account
    """
    user_option = input(display_formatter(t.ACC_UPDATE,
                                          account['id'],
                                          account['username'],
                                          account['password'],
                                          account['address'],
                                          account['acc_type']))

    if user_option == '1':  # Change Password
        is_updating = True

        while is_updating:
            new_password = input('NEW PASSWORD: ')
            validated_password = password_validator(new_password)

            if validated_password:
                confirm_password = input('REPEAT NEW PASSWORD: ')
                if new_password == confirm_password:
                    account['password'] = new_password
                    update_account(account)
                    print('Password changed!')
                    break
                else:
                    print(display_formatter(t.ERROR_MESSAGE, 'Password\'s did not match, please try again'))
                    continue

    elif user_option == '2':  # Change Address
        new_address = input('NEW ADDRESS: ')
        account['address'] = new_address
        update_account(account)


def delete_account(account: dict):
    """Function to confirm deletion of an account record

    Parameters:
        account: Dictionary of account"""

    user_choice = input(t.CONFIRM_DELETE)

    if user_choice == '1':  # Confirm delete
        delete_account_by_username(account['username'])
        print(f'Account id: {account['id']} has been deleted')


def refine_account_search(accounts: list[dict] | dict) -> dict:
    """ Function to refine account search and return account in json format

    Parameters:
        accounts: List of account dictionaries in json format or a singular
                  account dictionary.

    Return:
        An account dictionary
    """
    if type(accounts) is list:
        enumerated_accounts = enumerate_object(accounts)  # Returns an enumerated dictionary of accounts

        while True:
            for position, acc_json in enumerated_accounts.items():
                print_account(acc_json, position)

            try:
                user_choice = int(input(t.REFINE_SEARCH))
                if user_choice in enumerated_accounts.keys():
                    print_account(enumerated_accounts[user_choice])
                    acc_json = enumerated_accounts[user_choice]
                    return acc_json
                else:
                    break

            except ValueError:
                break

    else:
        print_account(accounts)  # Prints a single account if a dictionary
        return accounts


def account_search() -> dict:
    """Function to return an account dictionary, conditionally on user choice

    Returns:
        A dictionary of an account"""

    while True:
        user_choice = input(t.SEARCH_ACC_OPTION)

        if user_choice == '1':  # by id
            try:
                id_input = int(input('ID: '))
                data = return_accounts_by_id(id_input)
                if len(data) == 0:
                    print(display_formatter(t.ERROR_MESSAGE, 'No id\'s matched your search'))
                    continue

                else:
                    result_json = account_mapping(data)  # accounts - list[dict]
                    return refine_account_search(result_json)  # Returns single account dictionary

            except ValueError:
                print(display_formatter(t.ERROR_MESSAGE, 'No id\'s matched your search'))
                continue

        elif user_choice == '2':  # by username
            username_input = input('USERNAME: ')
            data = return_accounts_by_username(username_input)

            if len(data) == 0:
                print(display_formatter(t.ERROR_MESSAGE, 'No users matched your search'))
                break

            else:
                result_json = account_mapping(data)
                return refine_account_search(result_json)

        elif user_choice == '3':  # by acc type

            while True:
                acc_input = input(t.SEARCH_ACC_TYPE)

                if acc_input == '1':  # Search by admin
                    data = return_accounts_by_type('admin')

                    if len(data) == 0:
                        print(display_formatter(t.ERROR_MESSAGE, f'No admins in database'))
                        break

                    else:
                        result_json = account_mapping(data)  # accounts - list[dict]
                        return refine_account_search(result_json)  # Returns single account - dict

                elif acc_input == '2':  # Search by customer
                    data = return_accounts_by_type('customer')

                    if len(data) == 0:
                        print(display_formatter(t.ERROR_MESSAGE, f'No customers in database'))
                        break

                    else:
                        result_json = account_mapping(data)  # books - list[dict]
                        return refine_account_search(result_json)  # Returns single book - dict

                else:
                    break

        else:
            break  # Return to main menu
