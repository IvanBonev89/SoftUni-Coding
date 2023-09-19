sh = int(input())
dal = int(input())
vis = int(input())
s = sh * dal * vis
num_2 = 0
while True:
    numbers = input()
    if numbers != 'Done':
        num = int(numbers)
        num_2 += num
        diff = s - num_2
        if diff <= 0:
            print(f'No more free space! You need {abs(int(diff))} Cubic meters more.')
            break
    if numbers == 'Done' and s - int(num_2) > 0:
        diff = s- int(num_2)
        print(f"{abs(int(diff))} Cubic meters left.")
        break
