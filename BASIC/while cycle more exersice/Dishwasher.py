bootles = int(input())
kolichestvo_ml = bootles * 750
counter = 0
chisti_chinii = 0
chisti_tendjeri = 0
use = 0
sadove = input()
while sadove != 'End':
    num = int(sadove)
    counter += 1
    if counter % 3 != 0:
        use += num * 5
        chisti_chinii += num
        diff = kolichestvo_ml - use
    else:
        use += num * 15
        chisti_tendjeri += num
        diff = kolichestvo_ml - use
    if diff < 0:
        print(f"Not enough detergent, {abs(int(diff))} ml. more necessary!")
        break
    sadove = input()
    if use > kolichestvo_ml:
        print(f"Not enough detergent, {abs(int(diff))} ml. more necessary!")
        break
    if use <= kolichestvo_ml and sadove == "End":
        print("Detergent was enough!")
        print(f"{int(chisti_chinii)} dishes and {int(chisti_tendjeri)} pots were washed.")
        print(f"Leftover detergent {abs(int(diff))} ml.")
        break
