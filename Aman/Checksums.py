def byte_checksum(message):
    parity_byte = 0
    for c in message:
        parity_byte += ord(c)
        parity_byte = parity_byte % 256
    parity_byte = (~parity_byte + 1) % 256
    return message + chr(parity_byte)

message1 = "Hello"
message2 = byte_checksum(message1)
print(message2)

def verify_byte(message):
    parity_check = 0
    for c in message:
        parity_check += ord(c)
        parity_check = parity_check % 256
    if parity_check == 0:
        print("Message is valid")
    else:
        print("Message is compromised")

verify_byte(message2)
verify_byte("HelloT")

