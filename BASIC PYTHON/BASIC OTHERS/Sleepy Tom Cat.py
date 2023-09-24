# read user input

holiday_days = int(input())

#logic

work_days = 365 - holiday_days
work_play = work_days * 63
holiday_play = holiday_days * 127
total_play = work_play + holiday_play
left_play = abs(total_play - 30000)
h = left_play//60
m = left_play % 60

if total_play >= 30000:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
