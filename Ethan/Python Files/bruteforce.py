alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"


def decode(message, attempt=""):
    for key in range(len(alphabet)):
        newalphabet = alphabet[key:] + alphabet[:key]
        for i in range(len(message)):
            index = alphabet.find(message[i])
            if index < 0:
                attempt += message[i]
            else:
                attempt += newalphabet[index]
        print("Key: " + str(key) + " - ")


decode(message)

