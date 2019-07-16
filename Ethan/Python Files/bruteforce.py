
message = "0b1100_1001_1101_1111_0010_0100_0000_1000"



def decode(message):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for key in range(len(alphabet)):
        attempt = ""
        newalphabet = alphabet[key:] + alphabet[:key]
        for i in range(len(message)):
            index = alphabet.find(message[i])
            if index < 0:
                attempt += message[i]
            else:
                attempt += newalphabet[index]
        print("Key: " + str(key) + " - " + attempt)


decode(message)

