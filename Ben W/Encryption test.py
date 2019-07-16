def apply_rotate(message_list, key, block_size=4):
    cipher_list = ""
    bit_max = block_size*8
    for i in range(len_message_list)):
        chunk