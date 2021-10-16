# encryption.py
# Aarsh Shah, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

### Define your functions here
import string


def menu2(userchoice):
    """The encode function takes a message and encodes it into a """
    alphabet = string.ascii_lowercase

    message = input('Please enter the text to be processed: ').lower()
    if message.isalpha() == True:
        cipher_text = input(
            'Please enter the cipher text (alpha-numerical only): ').lower()
    else:
        print('The provided message is not valid please try again')
        menu2(userchoice)

    if cipher_text.isalnum() == True:
        # Might have to switch and get it to check if the cipher text exists within a dictionary or list
        cipher_text_no_dup = ''.join(dict.fromkeys(cipher_text))
        message = message.replace(' ', '')
        if len(cipher_text_no_dup) == 26:
            print('Your cipher is valid.')
            if userchoice == '1':
                encode(message, cipher_text_no_dup, alphabet)
            elif userchoice == '2':
                decode(message, cipher_text_no_dup, alphabet)
        else:
            print('The provided cipher is not 26 characters please try again')
            menu2(userchoice)
    else:
        print('The provided cipher is not alpha-numerical please try again')
        menu2(userchoice)


def encode(message, cipher_text_no_dup, alphabet):
    new_dic = {}
    iteration = 0
    for i in alphabet:
        new_dic[i] = cipher_text_no_dup[iteration]
        iteration += 1

    new_msg = ''
    for i in message:
        new_msg += new_dic[i]
    print(f'Your output is: {new_msg}')
    main_menu()


def decode(message, cipher_text_no_dup, alphabet):
    new_dic = {}
    iteration = 0
    for i in cipher_text_no_dup:
        new_dic[i] = alphabet[iteration]
        iteration += 1

    new_msg = ''
    for i in message:
        new_msg += new_dic[i]
    print(f'Your output is: {new_msg}')
    main_menu()


def main_menu():
    user_choice = input(
        'Would you like to:\nEncode your text (1)\nDecode your text (2)\nEnd the program (0):\n'
    )
    if user_choice == '1':
        menu2(user_choice)
    elif user_choice == '2':
        menu2(user_choice)
    elif user_choice == '0':
        print('Thank you for using the encryption program.')
        quit()
    else:
        print('Invalid input, try again')
        main_menu()


### Add your main program code here
print("ENDG 233 Encryption Program")
main_menu()
