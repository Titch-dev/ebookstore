# Regular expression module
import re
# Templates
import templates.templates as t


def return_to_menu():
    """Function to provide stall before returning to menu"""
    return input(display_formatter(t.CONFIRM_MESSAGE, 'Press enter to return to the main menu'))


def password_validator(password: str):
    """Function to validate user defined password

    Parameters:
        password: a string

    Returns:
        Boolean
    """
    # (?=.*[A-Z]) - ensures that at least one capital letter is present
    # (?=.*\d) - ensures at least one number is present
    # [A-Za-z\d@$!%*#?&]{6,} - Ensures there's a minimum of 6 characters
    password_pattern = r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}$'
    validated = re.match(password_pattern, password)

    if validated:
        return validated

    else:
        display_formatter(t.ERROR_MESSAGE, t.PASSWORD_VAL_ERROR)
        return validated


def display_formatter(template: str, *dynamic_vars: str | int):
    """Function to dynamically enter variables to display strings

    Parameters:
        template: string to format with variables
        *dynamic_vars: strings and integers to format template

    Returns:
        Concatenated string
    """
    return template.format(*dynamic_vars)


def enumerate_object(objects: list[dict]) -> dict:
    """Function to enumerate a list of json dictionary

    Parameters:
        objects: List of object json dictionary

    Returns:
        Dictionary of enumerated keys and json values
    """
    enumerated_objects = dict()
    for idx, obj in enumerate(objects, 1):
        enumerated_objects[idx] = obj
    return enumerated_objects
