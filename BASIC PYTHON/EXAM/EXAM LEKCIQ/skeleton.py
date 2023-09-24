# input

minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_meter = int(input())

minutes_1 = minutes * 60
total_record = minutes_1 + seconds
count = lenght / 100
total_seconds = count * seconds_meter
slow_count = lenght / 120
slow_seconds = slow_count * 2.5
total_time = total_seconds - slow_seconds
diff = abs(total_time - total_record)
# print
if total_record >= total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")