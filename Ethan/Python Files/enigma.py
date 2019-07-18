import math

# Message
message = input()
message = message.upper()

numb = []

for sign in message:
    number = ord(sign) - 65
    numb.append(number)

# Input settings
RotorI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
RotorII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
RotorIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
Reflektor = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
Plugboard = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]
RotIstart = 7
RotIIstart = 24
RotIIIstart = 0


# Shifting the start setting for the rotor
def shiftstart(seq, n):
    return seq[n:] + seq[:n]


# Shifting the rotors
def shift(seq, n, rn, numb):
    if rn == 1:
        n = -n % len(seq)

    elif rn == 2:
        n = - math.trunc(n / 25) % len(seq)

    elif rn == 3:
        n = - math.trunc(n / 675) % len(seq)

    return seq[n:] + seq[:n]


# Going back through the rotor after reflektion
def rotorrev(seq):
    rotorrev = ['empty'] * 26
    for i in range(26):
        rotorrev[seq[i]] = i

    return rotorrev


# Going through the rotor
def rotor(seq, rev, numb, rn):
    number = []
    Rotorreverse = ['empty'] * 26
    if rev == 0:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            number.append(rotation[numb[i]])

    elif rev == 1:
        for i in range(len(numb)):
            rotation = shift(seq, i, rn, numb)
            seqrev = rotorrev(rotation)
            number.append(seqrev[numb[i]])

    return number


# Going through the reflektor or plugboard
def RefPlug(list, numbIII):
    ref = []
    for i in range(len(numbIII)):
        ref.append(list[numbIII[i]])

    return ref


# Enigma
RotorIM = shiftstart(RotorI, RotIstart)
RotorIIM = shiftstart(RotorII, RotIIstart)
RotorIIIM = shiftstart(RotorIII, RotIIIstart)

Seq = RefPlug(Plugboard, numb)
SeqI = rotor(RotorIM, 0, Seq, 1)
SeqII = rotor(RotorIIM, 0, SeqI, 2)
SeqIII = rotor(RotorIIIM, 0, SeqII, 3)
SeqIV = RefPlug(Reflektor, SeqIII)
SeqVI = rotor(RotorIIIM, 1, SeqIV, 3)
SeqVII = rotor(RotorIIM, 1, SeqVI, 2)
SeqVIII = rotor(RotorIM, 1, SeqVII, 1)
SeqIX = RefPlug(Plugboard, SeqVIII)

# Message output
new_mes = []
for i in range(len(SeqIX)):
    word = chr(SeqIX[i] + 65)
    new_mes.append(word)

print(''.join(new_mes))
