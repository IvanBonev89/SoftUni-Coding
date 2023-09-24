num_1 = int(input())
num_2 = int(input())

for number in range (num_1, num_2 + 1):
    number_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")
