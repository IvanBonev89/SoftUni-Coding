# read user input

month = input()
nights = int(input())
price_studio = 0
price_apartament = 0

# logic

if month == 'May' or month == 'October':
    price_studio = 50
    price_apartament = 65
    if 7 < nights < 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.70
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartament = 68.70
    if nights > 14:
        price_studio *= 0.80
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartament = 77

if nights > 14:
    price_apartament *= 0.90

total_price_studio = price_studio * nights
total_price_apartmanet = price_apartament * nights
print(f"Apartment: {total_price_apartmanet:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")

