alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"

def decode(secretMessage):
    for key in range(len(alphabet)):
        attempt = ""
        newAlphabet = alphabet[key:] + alphabet[:key]
        for i in range(len(secretMessage)):
            index = alphabet.find(secretMessage[i])
            if index < 0:
                attempt += secretMessage[i]
            else:
                attempt += newAlphabet[index]
        print("key:" + str(key) + " - " + attempt)
decode(message)
