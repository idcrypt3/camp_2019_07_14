A = 0x5f
print(A)
print(hex(A))
print(bin(A))
B = 0b1000_0010_0100_0000_1010_0111_1001_1100
C = 0x82_40_a7_9c
if B == C:
    print("they are the same")
else:
    print("they're different")
numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
text = ""
for i in numbers:
    text += chr(i)
    for c in text:
        ord(c)
N = ord(c)
escape = “\x1b[“