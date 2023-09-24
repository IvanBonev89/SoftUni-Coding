# read user input
import math
serial = str(input())
time_episode = int(input())
time_relax = int(input())

# logical

time_lunch = 1/8 * (time_relax)
time_sleep = 1/4 * (time_relax)
time_serial = time_relax - time_lunch - time_sleep
free_time = math.ceil(abs(time_serial - time_episode))
# output print
if time_serial >= time_episode:
    print(f"You have enough time to watch {serial} and left with {free_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {free_time} more minutes.")
