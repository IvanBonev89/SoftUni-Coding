command = input()
coffee = 0
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffee += 1
        else:  # if command.isupper()
            coffee += 2
    command = input()

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")
