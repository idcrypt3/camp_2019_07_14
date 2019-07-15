alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne= ""
partialTwo = ""
newAlphabet = ""
myMessage = input("Please enter a message to encode ").lower()
key = int(input("Please enter a number to shift by, e.g. 2. A = c, b = d, and so on "))

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
for i in range(0, len(myMessage)):
    index = alphabet.find(myMessage[i])
    if index < 0:
        newMessage += myMessage[i]
    else:
        newMessage += newAlphabet[index]
print(newMessage)