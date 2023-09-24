fuel = str(input())
liters = int(input())

if fuel in ("Diesel Gasoline Gas"):
    if liters >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")

