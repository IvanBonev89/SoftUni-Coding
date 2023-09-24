n = int(input())
status = ''
character = ''
for i in range(n):
    command = input()
    for j in command:
        if j == "(" or j == ")":
            character += j
if character == "()" or character == "()()" or character == "()()()":
    status = "BALANCED"
else:
    status = "UNBALANCED"

print(status)

