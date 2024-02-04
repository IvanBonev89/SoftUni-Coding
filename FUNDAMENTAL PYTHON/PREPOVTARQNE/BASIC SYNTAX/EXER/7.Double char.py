new_text = ''
while True:
    text = input()
    if text == "End":
        break
    elif text != "SoftUni":
        for i in text:
            j = i+i
            new_text += j
        print(new_text)
        new_text = ''
