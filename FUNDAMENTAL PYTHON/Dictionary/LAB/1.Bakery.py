info = input().split(" ")
bakery = {}
for i in range(0,len(info), 2):
        food = info[i]
        quantities = int(info[i+1])
        bakery[food] = quantities

print(bakery)