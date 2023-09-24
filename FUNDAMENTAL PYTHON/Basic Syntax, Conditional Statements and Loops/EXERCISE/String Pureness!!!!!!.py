n = int(input())

for current_string in range(n):
    string1 = input()
    if "," in string1 or "." in string1 or "_" in string1:
        print(f"{string1} is not pure!")
    else:
        print(f"{string1} is pure.")
