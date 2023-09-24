# read user input

days = int(input())
type = input()
assessment = input()
price = 0
# logic

if days < 10:
    if type == 'room for one person':
        price = 18 * (days - 1)
    elif type == 'apartment':
        price = (25 * (days - 1)) * 0.70
    elif type == 'president apartment':
        price = (35 * (days - 1)) * 0.90
elif 10 < days < 15:
    if type == 'room for one person':
        price = 18 * (days - 1)
    elif type == 'apartment':
        price = (25 * (days - 1)) * 0.65
    elif type == 'president apartment':
        price = (35 * (days-1)) * 0.85
elif days > 15:
    if type == 'room for one person':
        price = 18 * (days - 1)
    elif type == 'apartment':
        price = (25 * (days-1)) * 0.50
    elif type == 'president apartment':
        price = (35 * (days-1)) * 0.80

if assessment == 'positive':
    price *= 1.25
elif assessment == 'negative':
    price *= 0.90

print(f'{price:.2f}')
