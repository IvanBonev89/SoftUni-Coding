# read user input
number = int(input())
if number <= 100:
    bonus_points = 5
elif number > 1000:
    bonus_points = number * 0.10
else:
    bonus_points = number * 0.20
if number % 2 == 0:
    extra_bonus_point = 1
elif number % 10 == 5:
    extra_bonus_point = 2
else:
    extra_bonus_point = 0

total_bonus_points = bonus_points + extra_bonus_point
total_number = number + total_bonus_points
print(total_bonus_points)
print(total_number)







