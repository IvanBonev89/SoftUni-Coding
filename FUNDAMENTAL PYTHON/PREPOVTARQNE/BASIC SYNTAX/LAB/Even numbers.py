n = int(input())
status = ""

for i in range(1,n+1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        status = "odd"
        break
if status != "odd":
    print("All numbers are even.")
