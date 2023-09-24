number_snow_balls = int(input())
result_max = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for best_ball in range(1,number_snow_balls+1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight / time) ** quality
    if result_max < result:
        result_max = result
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(result_max)} ({snowball_quality})")
