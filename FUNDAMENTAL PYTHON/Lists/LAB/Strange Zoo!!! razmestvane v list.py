tail = input()
body = input()
head = input()

full = [tail, body, head]

full[0], full[2] = full[2], full[0]

print(full)
