# input
import math
name = input()
seasons = int(input())
episodes = int(input())
time = float(input())

# logic

advertising = time * 0.2
total_episodes = seasons  * episodes
sum_time = total_episodes * time
total_advertising = advertising * total_episodes
special_time = seasons * 10
total_time = sum_time + special_time + total_advertising
total_time_math = math.floor(total_time)

#print
print(f"Total time needed to watch the {name} series is {total_time_math} minutes.")
