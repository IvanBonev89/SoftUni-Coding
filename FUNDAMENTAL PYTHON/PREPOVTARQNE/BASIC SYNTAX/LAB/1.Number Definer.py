#input
num = float(input())
status = ''

if num == 0:
    print("zero")
else:
    if num > 0:
        status = "positive"
    elif num < 0:
        status = "negative"
if num > 0 and num < 1:
    status = "small positive"
elif num < 0 and num > -1:
    status = "small negative"
elif num > 1000000:
    status = "large positive"
elif num < -1000000:
    status = "large negative"

print(status)