# read user input

hour = int(input())
minute = int(input())
hour_travel = int(input())
minute_travel = int(input())

# logic

time_exam = hour * 60 + minute
time_travel = hour_travel * 60 + minute_travel

if time_travel > time_exam:
    print ('Late')
elif time_exam - 30 <= time_travel <= time_exam:
    print ('On time')
elif time_exam - 30 > time_travel:
    print ('Early')

diff = abs(time_exam - time_travel)
hours = diff // 60
minutes = diff % 60

if  time_travel != time_exam and time_exam - 60 < time_travel < time_exam:
    print(f"{minutes} minutes before the start")
elif time_travel != time_exam and time_travel <= time_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_travel != time_exam and time_exam + 60 > time_travel > time_exam:
    print(f"{minutes} minutes after the start")
elif time_travel != time_exam and time_travel >= time_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")

