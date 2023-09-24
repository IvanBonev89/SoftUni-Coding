# read user input

budget = float(input())
season = input()
location = ''
vacantion = ''
is_valid = True
#logic
price = 0

if budget <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        price = 0.3 * budget
    elif season == 'winter':
        price = 0.7 * budget
    else:
        is_valid = False
elif 100 < budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        price = 0.4 * budget
    elif season == 'winter':
        price = 0.8 * budget
    else:
        is_valid = False
elif 100 < budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        price = 0.4 * budget
    elif season == 'winter':
        price = 0.8 * budget
    else:
        is_valid = False

elif 1000 < budget:
    location = 'Europe'
    if season == 'summer':
        price = 0.9 * budget
    elif season == 'winter':
        price = 0.9 * budget
    else:
        is_valid = False

if season == 'summer':
    vacantion = 'Camp'
elif season == 'winter':
    vacantion = 'Hotel'
else:
    is_valid = False

if location == 'Europe':
    vacantion = 'Hotel'

pass
#print
if is_valid:
 print(f"Somewhere in {location}")
 print(f"{vacantion} - {price:.2f}")
