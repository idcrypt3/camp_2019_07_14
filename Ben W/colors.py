text = "|"
escape = "\033["
for i in range(41, 47):
    color = str(i) + "m"
    colored_text = (escape + color + text)
    print(colored_text)



