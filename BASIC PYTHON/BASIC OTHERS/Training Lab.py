w = float(input())
h = float(input())
h_1 = h - 1
tables_red = int(h_1/0.7)
number_redove = int(w / 1.2)
total_number = tables_red * number_redove
total_number_with_lost = total_number - 3
print(int(total_number_with_lost))


