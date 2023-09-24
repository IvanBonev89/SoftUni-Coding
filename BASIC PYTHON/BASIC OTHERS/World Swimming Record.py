# read user input
import math
record_seconds = float(input())
track_meters = float(input())
time_for_meter = float(input())

#logical
slow = math.floor(track_meters//15)
time_slow = slow * 12.5
time_ivan = (track_meters * time_for_meter) + time_slow
range = time_ivan - record_seconds
#output print
if time_ivan < record_seconds:
    print(f" Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {range:.2f} seconds slower.")
