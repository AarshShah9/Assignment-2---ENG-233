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

    if cipher_text.isalnum() == True:
        # Might have to switch and get it to check if the cipher text exists within a dictionary or list
        cipher_text_nodup = ''.join(dict.fromkeys(cipher_text))
        if len(cipher_text_nodup) == 26:
            print('Your cipher is valid.')

        cipher_text_list = list(cipher_text_nodup)
        alphanumeric = {
            'a': cipher_text_list[0],
            'b': cipher_text_list[1],
            'c': cipher_text_list[2],
            'd': cipher_text_list[3],
            'e': cipher_text_list[4],
            'f': cipher_text_list[5],
            'g': cipher_text_list[6],
            'h': cipher_text_list[7],
            'i': cipher_text_list[8],
            'j': cipher_text_list[9],
            'k': cipher_text_list[10],
            'l': cipher_text_list[11],
            'm': cipher_text_list[12],
            'n': cipher_text_list[13],
            'o': cipher_text_list[14],
            'p': cipher_text_list[15],
            'q': cipher_text_list[16],
            'r': cipher_text_list[17],
            's': cipher_text_list[18],
            't': cipher_text_list[19],
            'u': cipher_text_list[20],
            'v': cipher_text_list[21],
            'w': cipher_text_list[22],
            'x': cipher_text_list[23],
            'y': cipher_text_list[24],
            'z': cipher_text_list[25]
        }

        for key, value in alphanumeric.items():
            # Replace key character with value character in string
            final_message = message.replace(key, value)
            print(final_message)

        else:
            print(
                'The provided cipher is not alpha-numerical please try again')
            encode()
    else:
        print('The provided cipher is not 26 characters please try again')
        encode()


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

# i = (-1)
#       for letter in cipher_text_nodup:
#             new_msg = cipher_text_nodup.replace(letter, alphabet)
#             print(new_msg)

# new_dic = {}
# iteration = 0
# for i in message:
#     new_dic[i] = alphabet[iteration]
#     iteration += 1

# new_msg = ''

# for i in cipher_text_nodup:
#     new_msg += new_dic[i]
# print(new_msg)

# main_menu()
