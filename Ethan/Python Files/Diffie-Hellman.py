def apply_shift(message, key):
    cipher = ""
    for c in message:
        number = ord(c) + key
        cipher += chr(number)
    return cipher


def remove_shift(cipher, key):
    message = ""
    for c in cipher:
        number = ord(c) - key
        message +=chr(number)
    return message


def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key
public_base = 8
public_modulus = 29


alice_private_key = 5
bob_private_key = 7
alice_message = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."

public_base = 8
public_modulus = 29
alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus

alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
alice_cipher = apply_shift(alice_message, alice_shared_key)
print(alice_cipher)

bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
alice_plaintext = remove_shift(alice_cipher, bob_shared_key)
print(alice_plaintext)

