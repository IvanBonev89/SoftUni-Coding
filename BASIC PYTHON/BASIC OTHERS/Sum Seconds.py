import math
time_first = int(input())
time_second = int(input())
time_third = int(input())

time_sum = time_first+time_second+time_third
sum_minutes = time_sum//60
sum_seconds = time_sum % 60
sum_minutes = math.floor(sum_minutes)

print(f"{sum_minutes}:{sum_seconds:02d}")














