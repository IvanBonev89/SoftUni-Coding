import math

number_tour = int(input())
start_points = int(input())
points = 0
etap = ''
winning = 0
for tennis in range(number_tour):
    etap = input()
    if etap == 'W':
        points += 2000
        winning += 1
    if etap == 'F':
        points += 1200
    if etap == 'SF':
        points += 720
total_points = start_points + points
avg_points = points / number_tour
avg_points = math.floor(avg_points)
percent_winning = winning / number_tour * 100
print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{percent_winning:.2f}%")
