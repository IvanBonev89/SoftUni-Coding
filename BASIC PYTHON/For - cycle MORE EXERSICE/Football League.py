stadium = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
for tour in range(1, fans + 1):
    sector = input()
    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == "V":
        v += 1
    elif sector == 'G':
        g += 1

p_a = a / fans * 100
p_b = b / fans * 100
p_v = v / fans * 100
p_g = g / fans * 100
p_fans = fans / stadium * 100

print(f"{p_a:.2f}%")
print(f"{p_b:.2f}%")
print(f"{p_v:.2f}%")
print(f"{p_g:.2f}%")
print(f"{p_fans:.2f}%")
