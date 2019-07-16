def sign_message(message, key):
    message_int = 0
    for c in message:
        message_int += ord(c)
    a = key[0]
    b = key[1]
    mac_tag = (a * message_int + b) % p
    return mac_tag


def check_mac(old_mac, new_mac):