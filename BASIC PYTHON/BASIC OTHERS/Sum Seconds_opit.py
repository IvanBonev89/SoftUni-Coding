# read user input
time_first = int(input())
time_second = int(input())
time_third = int(input())

#logic

total_time = time_first+time_second+time_third
minutes = total_time//60
seconds = total_time % 60
# output print
print(f"{minutes}:{seconds:02d}")
