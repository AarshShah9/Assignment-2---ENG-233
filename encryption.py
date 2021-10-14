# encryption.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

### Define your functions here
import string


def encode():
    """The encode function takes a message and encodes it into a """
    alphabet = string.ascii_lowercase
    numbers = string.digits

    message = input('Please enter the text to be processed: ').lower()
    cipher_text = input(
        'Please enter the cipher text (alpha-numerical only): ').lower()
    s = list(cipher_text)
    alphanumeric = {
        'a': cipher_text[0],
        'b': cipher_text[1],
        'c': cipher_text[2],
        'd': cipher_text[3],
        'e': cipher_text[4],
        'f': cipher_text[5],
        'g': cipher_text[6],
        'h': cipher_text[7],
        'i': cipher_text[8],
        'j': cipher_text[9],
        'k': cipher_text[10],
        'l': cipher_text[11],
        'm': cipher_text[12],
        'n': cipher_text[13],
        'o': cipher_text[14],
        'p': cipher_text[15],
        'q': cipher_text[16],
        'r': cipher_text[17],
        's': cipher_text[18],
        't': cipher_text[19],
        'u': cipher_text[20],
        'v': cipher_text[21],
        'w': cipher_text[22],
        'x': cipher_text[23],
        'y': cipher_text[24],
        'z': cipher_text[25]
    }

    if cipher_text.isalnum(
    ) == True:  # Might have to switch and get it to check if the cipher text exists within a dictionary or list
        cipher_text_nodupl = ''.join(dict.fromkeys(cipher_text))
        if len(cipher_text_nodupl) == 26:
            print('Your cipher is valid.')
        else:
            print(
                'The provided cipher is not alpha-numerical please try again')
            encode()
    else:
        print('The provided cipher is not 26 characters please try again')
        encode()

    for key, value in alphanumeric.items():
        # Replace key character with value character in string
        final_message = message.replace(key, value)
        print(final_message)

    main_menu()


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

print('Thank you for using the encryption program.')
