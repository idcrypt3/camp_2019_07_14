def pad_message(message,block_size=4):
    message_list = []
    chunk = 0
    block_count = len(message)//block_size + 1
    for c in range(block_count*block_size):
        chunk = chunk << 8
        if c < len(message):
            chunk += ord(message[c])
        if chunk.bit_length()>(block_size - 1)*8:
            message_list.append(chunk)
            chunk = 0
    return message_list

def rebuild_message(message_list, block_size=4):
    message = ""
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk>>(8*(block_size-1-c)))%2**8
            message += chr(number)
    return message

def apply_rotate(message_list,key,block_size=4):
    cipher_list = []
    bit__max = block_size*8
    for i in range(len(message_list)):
        chunk = message_list[i]
        carry = chunk % 2**key
        carry = carry << (bit__max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
    return cipher_list

def undo_rotate(cipher_list,key,block_size=4):
    message_list = []
    bit__max = block_size*8
    for i in range(len(cipher_list)):
        chunk = cipher_list[i]
        carry = chunk % 2**(bit__max - key)
        carry = carry << key
        cipher = (chunk >> (bit__max - key)) + carry
        message_list.append(cipher)
    return message_list

if __name__ == "__main__":
    message = "privete message"
    paded_message = pad_message(message)
    print("padded message: {}".format(paded_message))

    rotated_message = apply_rotate(paded_message,7)
    print("rotated_message: {}".format(rotated_message))

    unrotated_message = undo_rotate(rotated_message,7)
    print("unrotated: {}".format(unrotated_message))

    rebuilt_message = rebuild_message(unrotated_message)
    print("rebuilt message: {}".format(rebuilt_message))