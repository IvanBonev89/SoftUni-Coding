# read user input
product = input()
city = input()
quantity = float(input())
price = 0
# logic
if city == 'Sofia' and product == 'coffee':
    price = 0.50 * quantity
elif city == 'Sofia' and product == 'water':
    price = 0.80 * quantity
elif city == 'Sofia' and product == 'beer':
    price = 1.20 * quantity
elif city == 'Sofia' and product == 'sweets':
    price = 1.45 * quantity
elif city == 'Sofia' and product == 'peanuts':
    price = 1.60 * quantity

if city == 'Plovdiv' and product == 'coffee':
    price = 0.40 * quantity
elif city == 'Plovdiv' and product == 'water':
    price = 0.70 * quantity
elif city == 'Plovdiv' and product == 'beer':
    price = 1.15 * quantity
elif city == 'Plovdiv' and product == 'sweets':
    price = 1.30 * quantity
elif city == 'Plovdiv' and product == 'peanuts':
    price = 1.50 * quantity

if city == 'Varna' and product == 'coffee':
    price = 0.45 * quantity
elif city == 'Varna' and product == 'water':
    price = 0.70 * quantity
elif city == 'Varna' and product == 'beer':
    price = 1.10 * quantity
elif city == 'Varna' and product == 'sweets':
    price = 1.35 * quantity
elif city == 'Varna' and product == 'peanuts':
    price = 1.55 * quantity
# print user output

print (float(price))
