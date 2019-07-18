text = "|"
escape = "\033[0;"
for i in range(100):
    color = str(i) + "m"
    colored_text = (escape + color + text)
    print(colored_text)



