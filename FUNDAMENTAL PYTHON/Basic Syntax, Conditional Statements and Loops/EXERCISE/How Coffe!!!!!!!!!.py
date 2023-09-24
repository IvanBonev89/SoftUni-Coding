task = input()
coffe = 0
while task!= "END":
    if task.lower() in ["coding","cat", "dog","movie"]:
        coffe += 1
        if task.isupper():
            coffe += 1

    task = input()

if coffe <= 5:
    print(coffe)
else:
    print("You need extra sleep")



