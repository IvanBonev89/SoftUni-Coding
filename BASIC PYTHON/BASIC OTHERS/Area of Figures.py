# read user input
print("square, rectangle, circle or triangle")
figure = str(input())
# logic
if figure == "square":
    a = float(input())
    area = a * a
    result = (round(area, 3))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a*b
    result = (round(area, 3))
elif figure == "circle":
    r = float(input())
    from math import pi
    area = r * r * pi
    result = (round(area, 3))
elif figure == "triangle":
    x = float(input())
    h = float(input())
    area = (x * h)/2
    result = (round(area, 3))
else:
    print("wrong figure")
# output print
print(f"{result:.3f}")
