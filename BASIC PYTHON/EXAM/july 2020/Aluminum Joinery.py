# input

windows = int(input())
type = input()
delivery = input()
delivery_price = 0
# logic
price = 0
total_price = 0
final_price = 0
if type == '90X130':
    if 60 > windows > 30:
        price = 110 * 0.95
    elif windows > 60:
        price = 110 * 0.92
    elif 30 > windows > 10:
        price = 110
if type == '100X150':
    if 80 > windows > 40:
        price = 140 * 0.94
    elif windows > 80:
        price = 140 * 0.90
    elif 40 > windows > 10:
        price = 140
if type == '130X180':
    if 50 > windows > 20:
        price = 190 * 0.93
    elif windows > 50:
        price = 190 * 0.88
    elif 20 > windows > 10:
        price = 190
if type == '200X300':
    if 50 > windows > 25:
        price = 250 * 0.91
    elif windows > 50:
        price = 250 * 0.86
    elif 25 > windows > 10:
        price = 250

final_price = price * windows
if delivery == "With delivery":
    delivery_price = 60
else:
    delivery_price = 0

total_price = final_price + delivery_price
if windows > 99:
    total_price *= 0.96


# print
if windows < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
