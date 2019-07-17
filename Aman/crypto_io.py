import os, io

# uncomment the 3 lines below and replace the names of your files (do not include .py) and function defs
# leave "as name" as-is; this renames your functions so they are all compatible with this program,
# regardless of what you named them
from cipherprogram import ceasercipher as shift_cypher
from BlockCipherV2 import pad_message as block_pad, rebuild_message as block_rebuild
from BlockCipherV2 import apply_rotate as block_shift, undo_rotation as block_unshift
from DiffieHellmanV2 import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift

# here I set the private key used in Diffie-Hellman encryptions. Feel free to change it.
# the public_base is set to 8 and public_modulus 29, as on GamePlan. You can change those too.
dh_base = 8
dh_mod = 29
dh_private_key = 49
dh_public_key = dh_base ** dh_private_key % dh_mod

def main():
    # Feel free to change this intro msg to whatever you want
    print("Welcome Everybody")
    print("This is CryptIO, a Cryptographers dream package.")
    print("You can encrypt and decrypt messages made from other people or even yourself just to have fun")
    print("Keep in mind you need a secret key if you want to decrypt a message that someone else made.")

    # infinite loop runs until the user quits
    while True:
        print() # newline for readability
        choice = input("Type 1 to encrypt, 2 to decrypt, or 0 to quit: ")
        
        try: 
            choice = int(choice)
        except: 
            print("Sorry, that is not a valid choice.")
            continue

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            print("Thank you for using cryptoIO, a cryptographer's dream!")
            print("Have a good summer!")
            break
        else:
            print("Sorry, '{}' is not a valid choice. Pick 1, 2, or 0.".format(choice))
            continue

def encrypt():
    print("Preparing to encrypt...")
    data = get_encrypt_input()

    while True:
        file_name = input("Please enter the name you want to store you message under: ").strip()
        if "{}.txt".format(file_name) in os.listdir("msgs"):
            print("Someone already took that name so Sorry. Please choose another name")
            continue
        
        cypher = input(
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, or 3.".format(cypher))
            continue

        if cypher == 1:
            encrypted = shift_cypher(data[0], data[1])
            break
        elif cypher == 2:
            chunk_list = block_pad(data[0])
            encrypted = block_shift(chunk_list, data[1])
            encrypted = "\n".join(str(s) for s in encrypted)
            break
        elif cypher == 3:
            msg_public_key = dh_base ** data[1] % dh_mod
            shared_key = dh_shared_key(dh_private_key, msg_public_key)
            encrypted = dh_shift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    with io.open("msgs/{}.txt".format(file_name), 'w+', encoding="utf-8") as file:
        file.write(encrypted)
    print("Your message was successfully encrypted!\n")

def get_encrypt_input():
    msg = input("Please enter your secret message: ")
    key = get_key()
    return msg, key

def decrypt():
    print("Preparing to decrypt...")
    data = get_decrypt_input()

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, or 3.".format(cypher))
            continue

        if cypher == 1:
            decrypted = shift_cypher(data[0], -data[1])
            break
        elif cypher == 2:
            chunk_list = list(map(int, data[0].split("\n")))
            chunk_list = block_unshift(chunk_list, data[1])
            decrypted = block_rebuild(chunk_list)
            break
        elif cypher == 3:
            shared_key = dh_shared_key(data[1], dh_public_key)
            decrypted = dh_unshift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    print("The decrypted message is:\n'{}'".format(decrypted))

    return

def get_decrypt_input():
    localMsgs = os.listdir("msgs")
    for i in range(len(localMsgs)):
        n = i + 1   # '0' is the choice for manual input, so we offset the count by +1
        padding = " "
        if n <= 99:
            padding += " "
        if n <= 9:
            padding += " "
        print("{}{}: {}".format(n, padding, localMsgs[i]))
    print()

    while True:
        choice = input("Please choose a message from above to decrypt (or, type 0 for manual entry): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the encrypted message: ").strip()
            break
        elif choice <= len(localMsgs):
            with io.open("msgs/{}".format(localMsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))

    key = get_key()
    return msg, key

def get_key():
    while True:
        try:
            key = int(input("Please enter your secret key: "))
            break
        except ValueError:
            print("The secret key should be a number. Try again. ")
    return key

# This line automatically runs the main def when you start the program.
if __name__ == "__main__":
    main()

# Ideas for new features:
# - Include your name or contact info in the comments and/or opening scroll.
# - Write some messages or stories and encrypt and save them to disk for your family and friends to discover.
# - Include color codes - red for failed encryption, green for passed (see the lesson Hexadecimal\Character Codes).
# - This program includes functionality you haven't seen in the form of file I/O, string formatting, and imported
# modules. See if you understand what's going on and reference the online documentation if you don't.
# - Errors are handled, but the user navigation could be more friendly (e.g. allowing users to return to a previous menu
# rather than forcing them to stick with the choice to encrypt or decrypt, even if they change their mind). Try expand-
# ing it!
# Prevent the user from attempting a Ceaser shift greater than +-26, or use mod (%) to correct it

# Advanced features:
# - Create a puzzle for users to solve by slowly ramping up the difficulty (e.g., the key to a block cypher could be
# written in a ceaser cypher (as a word - remember, our ceaser cypher only substitutes letters), and that block cypher
# could have a clue to a Diffie-Hellman cypher, and...)
# - Display the checksum or hash of messages as they are encrypted and decrypted.
# You could even save the checksum/hash alongside the messages, so users know if a file has been modified.
# - Expand your cyphers with more options, or write a new one from internet tutorials.
