alphabet="abcdefghijklmnopqrstuvwxyz"
message= input("Please enter a message you wish to decode ")
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