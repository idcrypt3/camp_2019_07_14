message = "hello secret message here"
plugboard_output = ""
rotor1_output = ""
rotor2_output = ""
rotor3_output = ""
new_message = message
for i in range(len(message)):
    plugboard = [("b", "j"), ("c", "y"), ("d", "x"), ("e", "z"), ("f", "h"), ("g", "o"), ("l", "n"), ("m", "w"),
                 ("q", "v"), ("t", "u")]
    rotor1 = [("a", ""), ("b", ""), ("c", ""), ("d", "a"), ("e", ""), ("f", ""), ("g", ""), ("h", "w"), ("i", ""),
              ("j", ""), ("k", ""), ("l", ""), ("m", ""), ("n", ""), ("o", ""), ("p", ""), ("q", ""), ("r", ""),
              ("s", ""), ("t", ""), ("u", ""), ("v", "w"), ("x", ""), ("y", ""), ("z", "")]
    rotor2 = [("a", ""), ("b", ""), ("c", ""), ("d", ""), ("e", ""), ("f", ""), ("g", ""), ("h", "w"), ("i", ""),
              ("j", ""), ("k", ""), ("l", ""), ("m", ""), ("n", ""), ("o", ""), ("p", ""), ("q", ""), ("r", ""),
              ("s", ""), ("t", ""), ("u", ""), ("v", "w"), ("x", ""), ("y", ""), ("z", "")]
    rotor3 = [("a", ""), ("b", ""), ("c", ""), ("d", ""), ("e", ""), ("f", ""), ("g", ""), ("h", "w"), ("i", ""),
              ("j", ""), ("k", ""), ("l", ""), ("m", ""), ("n", ""), ("o", ""), ("p", ""), ("q", ""), ("r", ""),
              ("s", ""), ("t", ""), ("u", ""), ("v", "w"), ("x", ""), ("y", ""), ("z", "")]
    reflector = [("a", ""), ("b", ""), ("c", ""), ("d", ""), ("e", ""), ("f", ""), ("g", ""), ("h", "w"), ("i", ""),
                 ("j", ""), ("k", ""), ("l", ""), ("m", ""), ("n", ""), ("o", ""), ("p", ""), ("q", ""), ("r", ""),
                 ("s", ""), ("t", ""), ("u", ""), ("v", "w"), ("x", ""), ("y", ""), ("z", "")]
    letter = message[i]
    for c in range(len(plugboard)):
        if letter == plugboard[c][0]:
            new_message = new_message.replace(letter, plugboard[c][1])
print(new_message)

for i in range(len(new_message)):
    letter = new_message[i]
    for c in range(len(rotor1)):
        print("Letter = " + letter)
        print("Rotor 1 = " + rotor1[c][0])
        if letter == rotor1[c][0]:
            rotor1_output = rotor1_output.replace(letter, rotor1[c][1])
print(rotor1_output)


