''' Author- Jagu Manish || Python Programming Internship at Oasis Infobyte

------------------ TASK 3  - RANDOM PASSWORD GENERATOR -----------------------
Description:
For Beginners: Create a command-line password generator in Python that generates random passwords
based on user-defined criteria, such as length and character types
(letters, numbers, symbols). Allow users to specify password length and character set preferences.

For Advanced: Develop an advanced password generator with a graphical user interface (GUI) using Tkinter or PyQt. Enhance it by including options for password complexity, adherence to security rules, and clipboard integration for easy copying.
Key Concepts and Challenges:
Randomization: Learn how to generate random characters and strings.
User Input Validation: Validate user input for password length and character types.
Character Set Handling: Manage different character sets (letters, numbers, symbols).
GUI Design (for Advanced): Create an intuitive and user-friendly interface for password generation.
Security Rules (for Advanced): Implement rules for generating strong, secure passwords.
Clipboard Integration (for Advanced): Allow users to copy generated passwords to the clipboard for convenience.
Customization (for Advanced): Enable users to customize password generation further, e.g., excluding specific characters.

IDE used: Pycharm
Tip: Use VS Code for better performance.

'''

#importing modules
import random
import sys


def application_title():
    print("\n")
    print("                              ╔═══════════════════════════════════════════════════════╗")
    print("                              ║          P A S S W O R D   G E N E R A T O R          ║")
    print("                              ╚═══════════════════════════════════════════════════════╝")
    print("\n")


def application_note():
    print("         ╭────────────────────────────────────────────────────────────────────────────────────────────────╮")
    print("         │  Please utilize the 'Custom' (c) option to create a password tailored to your preferences,     │")
    print("         │  incorporating specified names and customization. Alternatively, utilize the 'Generalized' (g) │")
    print("         │  option to generate computer-generated values with the desired number of characters.           │")
    print("         │            Remember, it's essential to keep your passwords private and refrain from sharing    │")
    print("         │  them with others.                                                                             │")
    print("         ╰────────────────────────────────────────────────────────────────────────────────────────────────╯")


def generated_password(password):
    print("                             ═════════════════════════════════════════════════")
    print(f"     Your password is:                     {password}              ")
    print("                             ═════════════════════════════════════════════════")

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

def get_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Invalid input! The number must be at least 1.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def try_new_password():
    while True:
        try_new_password_input = input("Do you want to try a different password? Press 'e' to exit from the application (y/n): ").lower()
        if try_new_password_input in ['y', 'n', 'e']:
            if try_new_password_input == 'e':
                print("Beep.....Beep....Exiting the program...")
                sys.exit(0)
            return try_new_password_input == 'y'
        else:
            print("Invalid input! Please enter 'y' for yes, 'n' for no, or 'e' to exit.")


application_title()
application_note()

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_chars = ['@', '(', ')', '*', '!', '#', '+', '$', '%', '&']

while True:
    customization = input("Do you want to create a custom password or a generalized password? Enter 'c' for custom and 'g' for generalized: ").lower()

    if customization == 'g':
        n_letters = get_positive_int_input("How many letters do you want in your password? ")
        n_numbers = get_positive_int_input("How many numbers do you want in your password? ")
        n_special_chars = get_positive_int_input("How many symbols do you want in your password? ")

        try_new_password_choice = True
        while try_new_password_choice:
            user_password_list = [random.choice(letters) for _ in range(n_letters)]
            user_password_list += [random.choice(numbers) for _ in range(n_numbers)]
            user_password_list += [random.choice(special_chars) for _ in range(n_special_chars)]

            random.shuffle(user_password_list)
            password = "".join(user_password_list)
            generated_password(password)

            try_new_password_choice = try_new_password()

    elif customization == 'c':
        user_customization = get_yes_no_input("Do you want to use a name ('y') or generate with random letters ('n')? ")

        if user_customization == 'y':
            user_name = input("What name or word do you want to include in your password? ")
            capitalize_first_letter = get_yes_no_input("Do you want to capitalize the first letter ('y' or 'n')? ")
            include_special_character = get_yes_no_input("Do you want to include a special character in your password? ('y' or 'n') ")
            n_special_chars = get_positive_int_input("How many special characters do you want in your password? ") if include_special_character == 'y' else 0
            include_numbers = get_yes_no_input("Do you want to include numbers in your password? ('y' or 'n') ")
            n_numbers = get_positive_int_input("How many numbers do you want in your password? ") if include_numbers == 'y' else 0

            try_new_password_choice = True
            while try_new_password_choice:
                password_list = [user_name.capitalize() if capitalize_first_letter == 'y' else user_name.lower()]

                if include_special_character == 'y':
                    password_list += [random.choice(special_chars) for _ in range(n_special_chars)]

                if include_numbers == 'y':
                    password_list += [random.choice(numbers) for _ in range(n_numbers)]

                random.shuffle(password_list[1:])
                password = "".join(password_list)
                generated_password(password)

                try_new_password_choice = try_new_password()
                password = ""

        elif user_customization == 'n':
            n_letters = get_positive_int_input("How many letters do you want in your password? ")
            capitalize_first_letter = get_yes_no_input("Do you want to capitalize the first letter ('y' or 'n')? ")
            include_special_character = get_yes_no_input("Do you want to include a special character in your password? ('y' or 'n') ")
            n_special_chars = get_positive_int_input("How many special characters do you want in your password? ") if include_special_character == 'y' else 0
            include_numbers = get_yes_no_input("Do you want to include numbers in your password? ('y' or 'n') ")
            n_numbers = get_positive_int_input("How many numbers do you want in your password? ") if include_numbers == 'y' else 0

            try_new_password_choice = True
            while try_new_password_choice:
                password_list = [random.choice(letters) for _ in range(n_letters)]

                if capitalize_first_letter == 'y':
                    password_list[0] = password_list[0].upper()

                if include_special_character == 'y':
                    password_list += [random.choice(special_chars) for _ in range(n_special_chars)]

                if include_numbers == 'y':
                    password_list += [random.choice(numbers) for _ in range(n_numbers)]

                random.shuffle(password_list[1:])
                password = "".join(password_list)
                generated_password(password)

                try_new_password_choice = try_new_password()

    else:
        print("Invalid input! Please enter 'c' for custom or 'g' for generalized.")
