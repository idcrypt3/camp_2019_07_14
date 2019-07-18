def byte_checksum(message):
    parity_byte = 0
    for c in message:
        parity_byte += ord(c)
        parity_byte = parity_byte % 256
    parity_byte = (~parity_byte + 1) % 256
    return message + chr(parity_byte)


def verify_byte(message):
    parity_check = 0
    for c in message:
        parity_check += ord(c)
        parity_check = parity_check % 256
    if parity_check == 0:
        print("Message is valid")
    else:
        print("Message is compromised")


message_to_encode = input("Select a message to encode ")
print(message_to_encode + " is your message")
checksummed_message = byte_checksum(message_to_encode)
verify_byte(checksummed_message)
print("Now, if your message is stolen, it will be invalid. If you try to enter your message now, it will be invalid")
hack_attempt = input("Enter your message ")
verify_byte(hack_attempt)
