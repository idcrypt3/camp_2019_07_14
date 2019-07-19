import os, io, re

# uncomment the 3 lines below and replace the names of your files (do not include .py) and function defs
# leave "as name" as-is; this renames your functions so they are all compatible with this program,
# regardless of what you named them
from cipherprogram import ceasercipher as shift_cypher
from BlockCipherV2 import pad_message as block_pad, rebuild_message as block_rebuild
from BlockCipherV2 import apply_rotate as block_shift, undo_rotation as block_unshift
from DiffieHellmanV2 import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift
from ROT47Cipher import cipher_encryption as rot_encrypt, cipher_decryption as rot_decrypt
from RailFenceCipher import cipher_encryption as rail_encrypt, cipher_decryption as rail_decrypt
from Hash import pad_message as hash_pad, SHA256

# here I set the private key used in Diffie-Hellman encryptions. Feel free to change it.
# the public_base is set to 8 and public_modulus 29, as on GamePlan. You can change those too.
dh_base = 8
dh_mod = 29
dh_private_key = 49
dh_public_key = dh_base ** dh_private_key % dh_mod

def main():
    # Feel free to change this intro msg to whatever you want
    print("\033[1;36mWelcome Everybody")
    print("I am Aman Gupta, a 10th grader at Eastside Prep")
    print("This is CryptIO, a Cryptographers dream package.")
    print("You can encrypt and decrypt messages made from other people or even yourself just to have fun")
    print("Keep in mind you need a secret key if you want to decrypt a message that someone else made.")

    # infinite loop runs until the user quits
    while True:
        print() # newline for readability
        choice = input("\033[1;33mType 1 to encrypt, 2 to decrypt, 3 to run a security scan or 0 to quit: ")
        
        try:
            choice = int(choice)
        except: 
            print("Sorry, that is not a valid choice.")
            continue

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            compare_scan()
        elif choice == 0:
            print("\033[1;35mThank you for using cryptoIO, a cryptographer's dream!")
            print("Have a good summer!")
            break
        else:
            print("\033[1;31mSorry, '{}' is not a valid choice. Pick 1, 2, or 0.".format(choice))
            continue

def encrypt():
    print("\033[1;33mPreparing to encrypt...")
    data = get_encrypt_input()

    while True:
        file_name = input("\033[mPlease enter the name you want to store you message under: ").strip()
        if "{}.txt".format(file_name) in os.listdir("msgs"):
            print("\033[1;31mSomeone already took that name so Sorry. Please choose another name")
            continue
        
        cypher = input(
            "\033[1;35m1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\n4   : Rot47 Cipher\n5   : Rail-Fence Cipher\nPlease select a cypher (1, 2, 3, 4, or 5): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("\033[1,31mSorry, {} is not a valid choice. Pick 1, 2, 3, 4 or 5.".format(cypher))
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
        elif cypher == 4:
            encrypted = rot_encrypt(data[0], data[1])
            break
        elif cypher == 5:
            encrypted = rail_encrypt(data[0], data[1])
            break
        elif cypher == 0:
            return
        else:
            print("\033[1;31mThat is not a valid choice")
            continue
    try:
        with io.open("msgs/{}.txt".format(file_name), 'w+', encoding="utf-8") as file:
            file.write(encrypted)
    except ValueError:
        print("Error while writing the encrypted message file")

    try:
        with io.open(".manifest", "r", encoding="utf-8") as file:
            new_manifest = file.read()
        new_manifest += "\n" + file_name + ".txt\n" + hex(SHA256(hash_pad(encrypted)))
        with io.open(".manifest", "w+", encoding="utf-8") as file:
            file.write(new_manifest)
    except ValueError:
        print("Error in Security Scan while trying to write new manifest. Error in file {}".format(encrypted))



def get_encrypt_input():
    msg = input("Please enter your secret message: ")
    key = get_key()
    return msg, key

def decrypt():
    print("\033[1;34mPreparing to decrypt...")
    data = get_decrypt_input()

    while True:
        cypher = input(
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\n4   : Rot47 Cipher\n5   : Rail-Fence Cipher\nPlease select a cypher (1, 2, 3, 4, or 5): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("\033[1;31mSorry, {} is not a valid choice. Pick 1, 2, 3, 4, or 5.".format(cypher))
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
        elif cypher == 4:
            decrypted = rot_decrypt(data[0], data[1])
            break
        elif cypher == 5:
            decrypted = rail_decrypt(data[0], data[1])
            break
        elif cypher == 0:
            return

    print("\033[1;32mThe decrypted message is:\n'{}'".format(decrypted))

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
            print("\033[1;31mSorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the encrypted message: ").strip()
            break
        elif choice <= len(localMsgs):
            with io.open("msgs/{}".format(localMsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("\033[1;31mSorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))

    key = get_key()
    return msg, key

def get_key():
    while True:
        try:
            key = int(input("Please enter your secret key: "))
            break
        except ValueError:
            print("\033[1;31mThe secret key should be a number. Try again. ")
    return key

def scan():
    files = os.listdir("msgs")
    hash_list = ""
    for i in range(len(files)):
        with io.open("msgs/{}".format(files[i]), 'r', encoding="utf-8") as file:
            msg = file.read()
        hash = SHA256(hash_pad(msg))
        hash_list += files[i] + "\n" + hex(hash) + "\n"
    with io.open(".manifest", "w+", encoding="utf-8") as file:
        file.write(hash_list.strip())

def compare_scan():
    files = os.listdir("msgs")
    with io.open(".manifest", "r", encoding="utf-8") as file:
        manifest = file.read()
    manifest = manifest.split("\n")
    for f in files:
        i = manifest.index(f)
        with io.open("msgs/{}".format(f), 'r', encoding="utf-8") as file:
            message = file.read()
        hex_compare = hex(SHA256(hash_pad(message)))
        if hex_compare == manifest[i + 1]:
            print("Messages are fine")
            continue
        else:
            print("The Message {} has been compromised".format(f))
# This line automatically runs the main def when you start the program.
if __name__ == "__main__":
    main()

# Ideas for new features:
# - Errors are handled, but the user navigation could be more friendly (e.g. allowing users to return to a previous menu
# rather than forcing them to stick with the choice to encrypt or decrypt, even if they change their mind). Try expand-
# ing it!

# Advanced features:
# - Create a puzzle for users to solve by slowly ramping up the difficulty (e.g., the key to a block cypher could be
# written in a ceaser cypher (as a word - remember, our ceaser cypher only substitutes letters), and that block cypher
# could have a clue to a Diffie-Hellman cypher, and...)
# - Display the checksum or hash of messages as they are encrypted and decrypted.
# You could even save the checksum/hash alongside the messages, so users know if a file has been modified.
