import re
def cipher_encryption(message, key):
    message = message.replace(" ", "")

    railMatrix = []
    for i in range(key):
        railMatrix.append([])
    for row in range(key):
        for column in range(len(message)):
            railMatrix[row].append('.')

    row = 0
    check = 0
    for i in range(len(message)):
        if check == 0:
            railMatrix[row][i] = message[i]
            row += 1
            if row == key:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            railMatrix[row][i] = message[i]
            if row == 0:
                check = 0
                row = 1
    encryp_text = ""
    for i in range(key):
        for j in range(len(message)):
            encryp_text += railMatrix[i][j]

    encryp_text = re.sub(r"\.", "", encryp_text)
    return encryp_text

def cipher_decryption(message, key):
    message = message.replace(" ", "")

    railMatrix = []
    for i in range(key):
        railMatrix.append([])
    for row in range(key):
        for column in range(len(message)):
            railMatrix[row].append('.')

    row = 0
    check = 0
    for i in range(len(message)):
        if check == 0:
            railMatrix[row][i] = message[i]
            row += 1
            if row == key:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            railMatrix[row][i] = message[i]
            if row == 0:
                check = 0
                row = 1

    ordr = 0
    for i in range(key):
        for j in range(len(message)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                continue
            else:
                railMatrix[i][j] = message[ordr]
                ordr += 1
    for i in railMatrix:
        for column in i:
            print(column, end="")
        print("\n")

    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(message)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == key:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1

    decryp_text = re.sub(r"\.", "", decryp_text)
    return decryp_text

def main():
    message = input("What is your message? ")
    key = int(input("How many rails do you want (keep it under 20)"))
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print(cipher_encryption(message, key))
    elif choice == 2:
        print(cipher_decryption(message, key))
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()