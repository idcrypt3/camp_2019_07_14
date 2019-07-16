# Creating a shift cipher encryption function
def apply_shift(message, key):
    # declaring variable for cipher which is an empty string
    cipher = ""
    for c in message:
        number = ord(c) + key
        cipher += chr(number)
    # returning the encrypted message
    return cipher

# Creating a function to decrypt the encrypted message
def remove_shift(cipher,key):
    # Creating a empty string where the message will be stored
    message = ""
    # Iterating through every letter in the encrypted message and reversing the shift with the known key
    for c in cipher:
        number = ord(c) - key
        message += chr(number)
    # Returning the original message
    return message

def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key

# Variables that create the public key
public_base = 8
public_modulus = 29

# Setting the private keys of the recipients of the encrypted message. Used to decrypt the message
alice_private_key = 5
bob_private_key = 7
# Message that will be encrypted that Bob will decrypt
alice_message = "Hello Bob"

# Alice sends an encrypted message to Bob that he can decrypt
alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus
alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
# Next line of code will encrypt the message that Alice sent to Bob
alice_cipher = apply_shift(alice_message, alice_shared_key)
print(alice_cipher)
# Line is going to find shared key using Bob's private key and the public key from Alice.
bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
# Now bob will use the key to decrypt the cipher that Alice sent and he will have the original message
bob_message = remove_shift(alice_cipher, bob_shared_key)
# Printing the Original message before it was ciphered. This is the message that Bob decrypted from Alice
print(bob_message)
