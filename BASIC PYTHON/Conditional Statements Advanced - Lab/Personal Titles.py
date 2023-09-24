# read user input
age = float(input())
gender = input()

# logic
if age >= 16 and gender == "m":
    print("Mr.")
elif age < 16 and gender == "m":
    print('Master')
elif age >= 16 and gender == 'f':
    print('Ms.')
elif age < 16 and gender == "f":
    print('Miss')
