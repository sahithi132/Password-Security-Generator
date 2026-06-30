"""
=========================================================
        PASSWORD GENERATOR MODULE
=========================================================
Description:
Generates secure passwords based on user preferences.
=========================================================
"""

import random
import string


def generate_password(
    length=12,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True
):
    """
    Generate a secure random password.

    Parameters:
        length (int): Password length
        uppercase (bool): Include uppercase letters
        lowercase (bool): Include lowercase letters
        digits (bool): Include digits
        symbols (bool): Include special symbols

    Returns:
        str: Generated password
    """

    character_pool = ""
    password = []

    if uppercase:
        character_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if lowercase:
        character_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if digits:
        character_pool += string.digits
        password.append(random.choice(string.digits))

    if symbols:
        special_characters = "!@#$%^&*()-_=+[]{}<>?/|"
        character_pool += special_characters
        password.append(random.choice(special_characters))

    if not character_pool:
        raise ValueError("Select at least one character type.")

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print("Sample Password:")
    print(generate_password())