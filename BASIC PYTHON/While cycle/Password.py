name = input()
password = input()

while True:
    data = input()
    if data == password:
        print(f'Welcome {name}!')
        break
    else:
        continue
