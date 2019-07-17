def pad_message(message, block_size=4):
    message_list = []
    chunk = 0
    block_count = len(message)//block_size + 1
    for c in range(block_count*block_size):
        chunk = chunk << 8
        if c < len(message):
            chunk += ord(message[c])
        else:
            chunk += 0
        if chunk.bit_length() > (block_size-1)*8:
            message_list.append(chunk)
            chunk = 0
    return message_list


def rebuild_message(message_list, block_size=4):
    message = ""
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk >> (8*(block_size-1 - c))) % 2**8
            message += chr(number)
    return message


def apply_shift(message_list, key, block_size=4):
    cipher_list = []
    bit_max = block_size * 8
    for i in range(len(message_list)):
        chunk = message_list[i]
        carry = chunk % (2 ** key)
        carry = carry << (bit_max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
    return cipher_list


def undo_shift(cipher_list, key, block_size=4):
    message_list = []
    bit_max = block_size * 8
    for i in range(len(cipher_list)):
        chunk = cipher_list[i]
        carry = chunk % (2 ** (bit_max - key))
        carry = carry << key
        number = (chunk >> (bit_max - key)) + carry
        message_list.append(number)
    return message_list


plaintext = "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."
key = 20
text_list = pad_message(plaintext)
# print(text_list)
cipher_list = apply_shift(text_list, key)
# print(cipher_list)
cipher = rebuild_message(cipher_list)
# print(cipher)
message_list = undo_shift(cipher_list, key)
message = rebuild_message(message_list)
# print(message)
