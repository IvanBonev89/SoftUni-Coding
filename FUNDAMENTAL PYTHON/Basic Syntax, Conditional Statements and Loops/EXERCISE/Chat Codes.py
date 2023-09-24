number = int(input())
word = ""

for i in range(number):
    message = int(input())
    if message == 88:
        word = "Hello"
    elif message == 86:
        word = "How are you?"
    elif message!= 88 and message != 86 and message < 88:
        word = "GREAT!"
    elif message > 88:
        word = "Bye."
    print(word)


