
coffe = 0
while True:
    command = input()
    if command == "END":
        break
    else:
        if command.islower() and command in ["coding", "dog", "cat", "movie"]:
            coffe += 1
        elif command.isupper() and command in ["CODING", "DOG", "CAT", "MOVIE"]:
            coffe += 2
        else:
            continue

if coffe <= 5:
    print(coffe)
else:
    print("You need extra sleep")