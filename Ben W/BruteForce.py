alphabet="abcefghijklmnopqrstuvwxyz"
message= "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
def decode(myMessage):
    for key in range(len(alphabet)):
        attempt = ""
        newAlphabet = alphabet[key:] + alphabet[:key]
        for i in range(len(myMessage)):
            index = alphabet.find(myMessage[i])
            if index < 0:
                attempt += myMessage[i]
            else:
                attempt += newAlphabet[index]
        print("Key " + str(key) + "-" + attempt)
decode(message)