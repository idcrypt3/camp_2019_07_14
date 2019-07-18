def shift_cipher(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne= ""
    partialTwo = ""
    newAlphabet = ""


    if key == 0:
        newAlphabet = alphabet

    elif key > 0:
        # : cuts alphabet at key number
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

def main():
    myMessage = input("Please enter a message to encode ").lower()
    key = int(input("Please enter a number to shift by, e.g. 2. A = c, b = d, and so on "))
    print(shift_cipher(myMessage, key))

if __name__ == "__main__":
    main()
