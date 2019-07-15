alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""

message = input("Please enter a secret message: ").lower()
key = int(input("Please enter a number to shift by: "))

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

for i in range(0, len(myMessage)):
    index = alphabet.find(myMessage[i])

if index < 0:
    newMessage += myMessage[i]

else:
    newMessage += newAlphabet[index]

