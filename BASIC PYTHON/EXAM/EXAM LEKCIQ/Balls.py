# input
import math
n = int(input())
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_other = 0
#logic
points = 0
for balls in range (n):
    color = input()
    if color == 'red':
        points += 5
        count_red += 1
    elif color == 'orange':
        points += 10
        count_orange += 1
    elif color == 'yellow':
        points += 15
        count_yellow += 1
    elif color == 'white':
        points += 20
        count_white += 1
    elif color == 'black':
        points /= 2
        points = math.floor(points)
        count_black += 1
    else:
        points += 0
        count_other += 1


#print

print(f"Total points: {points}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_other}")
print(f"Divides from black balls: {count_black}")
