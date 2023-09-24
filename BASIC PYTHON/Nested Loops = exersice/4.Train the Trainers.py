n = int(input())
name = input()
sum = 0
avg_sum = 0
count = 0
avg_sum_2 = 0
while name != 'Finish':
    for i in range(n):
        ocenka = float(input())
        sum += ocenka
    avg = sum / n
    count += 1
    avg_sum += avg
    print(f'{name} - {avg:.2f}.')
    name = input()
    sum = 0

if name == 'Finish':
 avg_sum_2 = avg_sum / count
 print(f"Student's final assessment is {avg_sum_2:.2f}.")

