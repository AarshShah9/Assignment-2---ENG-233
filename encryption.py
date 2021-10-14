# encryption.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

# run_program = True


### Define your functions here
def encode():
    user_message = input('Please enter the text to be processed: ').lower()
    cipher_text = input(
        'Please enter the cipher text (alpha-numerical only): ').lower()
    cipher_check = cipher_text.isalnum()
    if cipher_check == True:
        cipher_text
    else:
        print('The provided cyper is not alpha-numerical please try again')
        encode()
    # for letter in alphabet:


def decode():
    pass


def end_program():
    quit()


def main_menu():
    user_choice = input(
        'Would like to encode your text (1)\nDecode your text (2)\nEnd the program (0): '
    )
    if user_choice == '1':
        encode()
    elif user_choice == '2':
        decode()
    elif user_choice == '0':
        end_program
    else:
        print('Invalid input, try again')
        main_menu()


main_menu()

print("ENDG 233 Encryption Program")

### Add your main program code here

alphabet = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': '',
    'h': '',
    'i': '',
}

print('Thank you for using the encryption program.')
