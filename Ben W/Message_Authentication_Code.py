def sign_message(message, key):
    message_int = 0
    for c in message:
        message_int += ord(c)
    print(message_int)
    a = key[0]
    b = key[1]
    mac_tag = (a * message_int + b) % p
    return mac_tag

p = 491
message = "Hello World"
key = [15, 30]
mac = sign_message(message, key)


def check_mac(old_mac, new_mac):
    if old_mac == new_mac:
        print("Message is valid")
    else:
        print("Message is compromised")


message_1 = "Hello World"
message_2 = "Hello world"

mac_1 = sign_message(message_1, key)
mac_2 = sign_message(message_2, key)

check_mac(mac, mac_1)
check_mac(mac, mac_2)

