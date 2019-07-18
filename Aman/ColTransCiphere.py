def cipher_encryption():
    msg = input("Enter Plain Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    kywrd_num_list = keyword_num_assign(key)

    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    print()
    print("-------------------------")

    extra_letters = len(msg) % len(key)
    dummy_characters = len(key) - extra_letters

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "."


    num_of_rows = int(len(msg) / len(key))

    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()

    num_loc = get_number_location(key, kywrd_num_list)

    print(num_loc)

    cipher_text = ""
    k = 0
    for i in range(num_of_rows):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        k += 1

    print("Cipher Text: {}".format(cipher_text))


def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)

    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init

    return kywrd_num_list


def cipher_decryption():
    msg = input("Enter Cipher Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    kywrd_num_list = keyword_num_assign(key)

    num_of_rows = int(len(msg) / len(key))

    num_loc = get_number_location(key, kywrd_num_list)

    arr = [[0] * len(key) for i in range(num_of_rows)]

    plain_text = ""
    k = 0
    itr = 0


    for i in range(len(msg)):
        d = 0
        if k == len(key):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(num_of_rows):
            arr[j][d] = msg[itr]
            itr += 1
        if itr == len(msg):
            break
        k += 1
    print()

    for i in range(num_of_rows):
        for j in range(len(key)):
            plain_text += str(arr[i][j])

    print("Plain Text: " + plain_text)


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("Encryption")
        cipher_encryption()
    elif choice == 2:
        print("Decryption")
        cipher_decryption()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()