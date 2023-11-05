string = input().split(", ")
int_numbers = [int(a) for a in string]
positive = []
negative = []
even = []
odd = []
for i in int_numbers:
    if i  >= 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

print("Positive: ", end="")
print(*positive, sep=", ")
print("Negative: ", end="")
print(*negative, sep=", ")
print("Even: ", end="")
print(*even, sep=", ")
print("Odd: ", end="")
print(*odd, sep=", ")