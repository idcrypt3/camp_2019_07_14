def cipher_encryption(message, key):
    encryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)

    return encryp_text

def cipher_decryption(message, key):
    decryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) - key
        if ord(message[i]) == 32:
            decryp_text += " "
        elif temp < 32:
            temp += 94
            decryp_text += chr(temp)
        else:
            decryp_text += chr(temp)

    return decryp_text

def main():
    message = input("What is your message? ")
    key = int(input("What is your key? "))
    choice = int(input("1. Encruption\n2. Decryption\n Choose(1,2): "))
    if choice == 1:
        print(cipher_encryption(message, key))
    elif choice == 2:
        print(cipher_decryption(message, key))
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()
