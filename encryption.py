# encryption.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

### Define your functions here


# def characters(letter):
#     alphabet = {
#         'a': letter[0],
#         'b': letter[1],
#         'c': letter[2],
#         'd': letter[3],
#         'e': letter[4],
#         'f': letter[5],
#         'g': letter[6],
#         'h': letter[7],
#         'i': letter[8],
#         'j': letter[9],
#         'k': letter[10],
#         'l': letter[11],
#         'm': letter[12],
#         'n': letter[13],
#         'o': letter[14],
#         'p': letter[15],
#         'q': letter[16],
#         'r': letter[17],
#         's': letter[18],
#         't': letter[19],
#         'u': letter[20],
#     }

#     numbers = {}


def encode():
    """The encode function takes a message and encodes it into a """
    user_message = input('Please enter the text to be processed: ').lower()
    cipher_text = input(
        'Please enter the cipher text (alpha-numerical only): ').lower()
    cipher_check1 = cipher_text.isalnum(
    )  # Might have to switch and get it to check if the cipher text exists within a dictionary or list
    if cipher_check1 == True:
        cipher_text_nodupl = ''.join(dict.fromkeys(cipher_text))
    else:
        print('The provided cipher is not alpha-numerical please try again')
        encode()

    if cipher_text_nodupl.len() == 26:
        print('Your cipher is valid.')
        encoded_message = ''
        print(f'Your output is: {encoded_message}')
    else:
        print('The provided cipher is not 26 characters please try again')
        encode()
    
    letter = cipher_text_nodupl
    alphabet = {
        'test': 'a',
        'b': letter[1],
        'c': letter[2],
        'd': letter[3],
        'e': letter[4],
        'f': letter[5],
        'g': letter[6],
        'h': letter[7],
        'i': letter[8],
        'j': letter[9],
        'k': letter[10],
        'l': letter[11],
        'm': letter[12],
        'n': letter[13],
        'o': letter[14],
        'p': letter[15],
        'q': letter[16],
        'r': letter[17],
        's': letter[18],
        't': letter[19],
        'u': letter[20],
    }
    
    for letters, value in alphabet:
        message1 = 

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
