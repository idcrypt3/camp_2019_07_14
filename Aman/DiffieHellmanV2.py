def apply_shift(message, key):
    cipher = ""
    for c in message:
        number = ord(c) + key
        cipher += chr(number)
    return cipher

def remove_shift(cipher,key):
    message = ""
    for c in cipher:
        number = ord(c) - key
        message += chr(number)
    return message

def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key

public_base = 8
public_modulus = 29

alice_private_key = 5
bob_private_key = 7
alice_message = input("What message do you want to encrypt then decrypt? ")

alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus
alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
alice_cipher = apply_shift(alice_message, alice_shared_key)
print(alice_cipher)
bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
bob_message = remove_shift(alice_cipher, bob_shared_key)
print(bob_message)
