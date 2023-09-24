task = input()
coffe = 0
while task!= "END":
    if task in ["coding","cat", "dog","movie"]:
        coffe += 1
    elif task in ["CODING", "CAT", "DOG", "MOVIE"]:
        coffe += 2

    task = input()

if coffe <= 5:
    print(coffe)
else:
    print("You need extra sleep")



