import string
from time import sleep

alphabet = string.ascii_lowercase

def decrypt():
    print("Welcome to Caesar Cipher Decrypter.\n")
    encrypted_message = input('Enter the message you want to decrypt : ').strip()
    print()
    key = int(input('Enter the key to decrypt : '))

    decrypted_message = ''

    for z in encrypted_message:

        if z in alphabet:
            position = alphabet.find(z)
            new_position = ( position - key ) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character

        else:
            decrypted_message += z

    print('\nPlease wait while your message is being decrypted....\n')
    sleep(5)
    print('Almost Done...')
    sleep(2)
    print('\nYour Decrypted message is : \n',decrypted_message)


decrypt()





