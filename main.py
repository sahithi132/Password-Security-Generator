"""
=========================================================
        PASSWORD SECURITY GENERATOR - MAIN PROGRAM
=========================================================
Author      : Sahithi
Description : Main application for generating secure
              passwords and checking password strength.
=========================================================
"""

import os
from password_generator import generate_password
from strength_checker import evaluate_password


class PasswordSecurityApp:

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display_title():
        print("=" * 60)
        print("        PASSWORD SECURITY GENERATOR")
        print("=" * 60)

    @staticmethod
    def menu():
        print("\n1. Generate Secure Password")
        print("2. Check Password Strength")
        print("3. Exit")

    @staticmethod
    def generate_password_option():

        print("\nGenerate Secure Password")
        print("-" * 60)

        try:
            length = int(input("Enter password length (8-64): "))

            if length < 8 or length > 64:
                print("\nPassword length must be between 8 and 64.")
                return

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        uppercase = input("Include Uppercase Letters? (Y/N): ").strip().lower() == "y"
        lowercase = input("Include Lowercase Letters? (Y/N): ").strip().lower() == "y"
        digits = input("Include Numbers? (Y/N): ").strip().lower() == "y"
        symbols = input("Include Special Characters? (Y/N): ").strip().lower() == "y"

        if not any([uppercase, lowercase, digits, symbols]):
            print("\nSelect at least one character type.")
            return

        password = generate_password(
            length=length,
            uppercase=uppercase,
            lowercase=lowercase,
            digits=digits,
            symbols=symbols
        )

        print("\n" + "=" * 60)
        print("Generated Password")
        print("=" * 60)
        print(password)

        result = evaluate_password(password)

        print("\nPassword Analysis")
        print("-" * 60)
        print(f"Strength : {result['strength']}")
        print(f"Score    : {result['score']}/5")
        print(f"Entropy  : {result['entropy']} bits")

    @staticmethod
    def strength_checker_option():

        print("\nPassword Strength Checker")
        print("-" * 60)

        password = input("Enter Password: ")

        if password == "":
            print("Password cannot be empty.")
            return

        result = evaluate_password(password)

        print("\n" + "=" * 60)
        print("Password Analysis")
        print("=" * 60)

        print(f"Password : {password}")
        print(f"Strength : {result['strength']}")
        print(f"Score    : {result['score']}/5")
        print(f"Entropy  : {result['entropy']} bits")

        print("\nSuggestions:")

        if result["suggestions"]:
            for item in result["suggestions"]:
                print(f"• {item}")
        else:
            print("Excellent! Your password is highly secure.")

    def run(self):

        while True:

            self.clear_screen()

            self.display_title()

            self.menu()

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == "1":
                self.generate_password_option()

            elif choice == "2":
                self.strength_checker_option()

            elif choice == "3":
                print("\nThank you for using Password Security Generator.")
                print("Stay Secure!")
                break

            else:
                print("\nInvalid choice.")

            input("\nPress Enter to continue...")


def main():
    app = PasswordSecurityApp()
    app.run()


if __name__ == "__main__":
    main()