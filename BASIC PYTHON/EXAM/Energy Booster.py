fruit = input()
size = input()
sets = int(input())
total_price = 0
price = 0
if fruit == 'Watermelon' and size == 'small':
    price = 56 * 2
    total_price = price * sets
elif fruit == 'Mango' and size == 'small':
    price = 36.66 * 2
    total_price = price * sets
elif fruit == 'Pineapple' and size == 'small':
    price = 42.10 * 2
    total_price = price * sets
elif fruit == 'Raspberry' and size == 'small':
    price = 20 * 2
    total_price = price * sets

if fruit == 'Watermelon' and size == 'big':
    price = 28.70 * 5
    total_price = price * sets
elif fruit == 'Mango' and size == 'big':
    price = 19.60 * 5
    total_price = price * sets
elif fruit == 'Pineapple' and size == 'big':
    price = 24.80 * 5
    total_price = price * sets
elif fruit == 'Raspberry' and size == 'big':
    price = 15.20 * 5
    total_price = price * sets

if 400 <= total_price <= 1000:
    total_price *= 0.85
if total_price > 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")
