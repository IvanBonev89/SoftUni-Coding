# input
import math

days = int(input())
kilometers = float(input())
total_kilometers = kilometers

#logic
for i in range(1, days+1):
    percent = float(input())
    kilometers_percent = (percent/100) * kilometers
    kilometers += kilometers_percent
    total_kilometers += kilometers
if total_kilometers >= 1000:
    diff = abs(total_kilometers - 1000)
    diff_format = math.ceil(diff)
    print(f"You've done a great job running {diff_format} more kilometers!")
else:
    diff = abs(1000 - total_kilometers)
    diff_format = math.ceil(diff)
    print(f"Sorry Mrs. Ivanova, you need to run {diff_format} more kilometers")
