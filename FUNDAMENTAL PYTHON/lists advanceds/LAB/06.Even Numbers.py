def even_num(numbers):
    even_list = []
    number_list = list(map(int, numbers))
    for i, num in enumerate(number_list):
        if num % 2 == 0:
            even_list.append(i)
    return even_list



numbers = input().split(", ")
print(even_num(numbers))