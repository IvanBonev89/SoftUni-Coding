# input

size = input()
color = input()
number = int(input())
price = 0

# logic

if size == 'Large':
    if color == "Red":
        price = 16
    elif color == "Green":
        price = 12
    elif color == "Yellow":
        price = 9
elif size == "Medium":
    if color == "Red":
        price = 13
    elif color == "Green":
        price = 9
    elif color == "Yellow":
        price = 7
elif size == "Small":
    if color == "Red":
        price = 9
    elif color == "Green":
        price = 8
    elif color == "Yellow":
        price = 5

total_price = number * price
cost = total_price * 0.35
profit = total_price - cost
print(f"{profit:.2f} leva.")
