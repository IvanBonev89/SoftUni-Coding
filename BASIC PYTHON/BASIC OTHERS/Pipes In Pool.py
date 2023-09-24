# read user input

v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

#logic
p1_water = p1*h
p2_water = p2*h
full_water = p1_water+p2_water
water_level_percent = (full_water / v) * 100
p1_percent = (p1_water/(p1_water+p2_water)) * 100
p2_percent = (p2_water/(p1_water+p2_water))* 100
over_liters = abs(full_water - v)

if v >= full_water:
    print(f"The pool is {water_level_percent}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {over_liters} liters.")

