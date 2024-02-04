number = int(input())
text = ''
status = ""

for i in range(number):
    status = ''
    text = input()
    for j in text:
        if j == "," or j == "." or j == "_":
            print(f"{text} is not pure!")
            status = "invalid"
            break
    if status != "invalid":
        print(f"{text} is pure.")

