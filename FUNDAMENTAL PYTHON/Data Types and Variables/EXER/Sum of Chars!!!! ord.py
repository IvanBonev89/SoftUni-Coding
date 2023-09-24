numbers = int(input())
sum = 0
for i in range(1,numbers+1):
    letter = input()
    asc = ord(letter)
    sum += asc

print(f"The sum equals: {sum}")

