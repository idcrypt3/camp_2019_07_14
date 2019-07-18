numbers = [0x69, 0x44, 0x54, 0x65, 0x63, 0x68]
text = ""
for i in numbers:
    text += chr(i)
print(text)
for c in text:
    N = ord(c)
    print(hex(N))

escape = "\x1b["
color = "36m"
colored_text = escape + color + text
print(colored_text)
