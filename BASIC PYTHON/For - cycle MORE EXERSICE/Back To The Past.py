money = float(input())
year = int(input())
cost = 0
age = 18

for time_travel in range(1800, year+1):
    if time_travel % 2 == 0:
        cost += 12000
        if time_travel > 1800:
            age+=1
    else:
        age += 1
        cost += 12000 + (50 * age)

diff = abs(money - cost)
if money >= cost:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

