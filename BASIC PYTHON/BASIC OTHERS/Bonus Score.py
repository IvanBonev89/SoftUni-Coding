number = int(input())
if number <= 100:
    bonus_point = 5
elif number > 1000:
    bonus_point = number * 0.1
else:
    bonus_point = number * 0.2
if number % 2 == 0:
    bonus_point_2 = 1
elif number % 10 == 5:
    bonus_point_2 = 2
else:
    bonus_point_2 = 0
total_bonus = bonus_point+bonus_point_2
total_number = number + bonus_point + bonus_point_2
print(total_bonus)
print(total_number)
