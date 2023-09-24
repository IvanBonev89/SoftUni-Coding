number = int(input())
large_num = ""
digits = sorted(str(number), reverse= True)

for i in digits:
    large_num += i

print(large_num)


