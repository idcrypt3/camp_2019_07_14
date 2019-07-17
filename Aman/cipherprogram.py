def main():
    message = input("Please enter a secret message: ").lower()
    key = int(input("Please enter a number to shift by: "))
    print(ceasercipher(message, key))

def ceasercipher(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo = ""
    newAlphabet = ""

    if key == 0:
        newAlphabet = alphabet

    elif key > 0:
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
        newAlphabet = partialTwo + partialOne

    else:
        partialOne = alphabet[:(26 + key)]
        partialTwo = alphabet[(26 + key):]
        newAlphabet = partialTwo + partialOne

    newMessage = ""

    for i in range(0, len(message)):
        index = alphabet.find(message[i])

        if index < 0:
            newMessage += message[i]

        else:
            newMessage += newAlphabet[index]

    return newMessage

if __name__ == "__main__":
    main()
