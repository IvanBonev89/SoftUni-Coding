budget = 0
while True:
    place = input()
    if place == 'End':
        break
    price = float(input())
    budget = 0
    while True:
        money = float(input())
        budget += money
        if budget >= price:
            print(f"Going to {place}!")
            break
