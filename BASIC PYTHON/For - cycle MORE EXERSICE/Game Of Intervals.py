# input
moves = int(input())
# logic
result = 0
gr1 = 0
gr2 = 0
gr3 = 0
gr4 = 0
gr5 = 0
invalid = 0

for game in range(1, moves + 1):
    num = int(input())
    if 0 <= num <= 9:
        result += num * 0.2
        gr1 += 1
    elif 10 <= num <= 19:
        result += num * 0.3
        gr2 += 1
    elif 20 <= num <= 29:
        result += num * 0.4
        gr3 += 1
    elif 30 <= num <= 39:
        result += 50
        gr4 += 1
    elif 40 <= num <= 50:
        result += 100
        gr5 += 1
    else:
        result /= 2
        invalid += 1

p_gr1 = gr1 / moves * 100
p_gr2 = gr2 / moves * 100
p_gr3 = gr3 / moves * 100
p_gr4 = gr4 / moves * 100
p_gr5 = gr5 / moves * 100
p_invalid = invalid / moves * 100
# output
print(f"{result:.2f}")
print(f"From 0 to 9: {p_gr1:.2f}%")
print(f"From 10 to 19: {p_gr2:.2f}%")
print(f"From 20 to 29: {p_gr3:.2f}%")
print(f"From 30 to 39: {p_gr4:.2f}%")
print(f"From 40 to 50: {p_gr5:.2f}%")
print(f"Invalid numbers: {p_invalid:.2f}%")
