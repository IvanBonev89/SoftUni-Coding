target = 10000
total_steps = 0
while True:
    steps = input()
    if steps == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        if total_steps >= target:
            diff = total_steps - target
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        diff = target - total_steps
        print(f"{diff} more steps to reach goal.")
        break
    else:
        total_steps += int(steps)
    if total_steps >= target:
        diff = total_steps - target
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break
    else:
        continue
