## Code snippet 1
def pad_message(message, block_size=4):
    # Take string message as input and return blocks of message bytes (integers)
    message_list = []
    chunk = 0
    block_count = len(message) // block_size + 1
    for c in range(block_count * block_size):
        # Shift byte right to make space for the next byte. Most significant bit is from the first character!
        chunk = chunk << 8
        if c < len(message):
            chunk += ord(message[c])
        else:
            chunk += 0
        # Add the chunk if it exceeds block size - 1 (since the next character would push it past the block size)
        if chunk.bit_length() > (block_size - 1) * 8:
            message_list.append(chunk)
            chunk = 0
    return message_list


## Code snippet 2
def rebuild_message(message_list, block_size=4):
    message = ""
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk >> (8 * (block_size - 1 - c))) % 2**8
            message += chr(number)
    return message


## Code snippet 3
def apply_shift(message_list, key, block_size=4):
    # Shift characters up Unicode value based on key value and block count
    cipher_list = []
    bit_max = block_size * 8
    for i in range(len(message_list)):
        # Iterate through each chunk in the message list
        chunk = message_list[i]
        # Rotate the bits in the chunk
        carry = chunk % (2 ** key)
        carry = carry << (bit_max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
    return cipher_list


## Code snippet 4
def undo_shift(cipher_list, key, block_size=4):
    # Rotate bits back to original position
    message_list = []
    bit_max = block_size * 8
    for i in range(len(cipher_list)):
        # Iterate through each chunk in the message list
        chunk = cipher_list[i]
        # Rotate the bits in the chunk
        carry = chunk % (2 ** (bit_max - key))
        carry = carry << key
        number = (chunk >> (bit_max - key)) + carry
        message_list.append(number)
    return message_list


## Code snippet 5
plaintext = "abcdefGHIJKLMNOpqr!@#$%123"
# Set the key as the number of bits to rotate in each block
key = 20
text_list = pad_message(plaintext)
# print(text_list)
cipher_list = apply_shift(text_list, key)
# print(cipher_list)
cipher = rebuild_message(cipher_list)
print(cipher)
message_list = undo_shift(cipher_list, key)
message = rebuild_message(message_list)
print(message)