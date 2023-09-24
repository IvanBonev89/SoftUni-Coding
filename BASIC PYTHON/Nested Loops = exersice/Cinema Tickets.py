count_student = 0
count_standart = 0
count_kid = 0
count_student_total = 0
count_standart_total = 0
count_kid_total = 0
total_tickets = 0
total_total = 0
percent_student = 0
percent_standart = 0
percent_kid = 0
bilet = ''
is_valid = False
while True:

    movie = input()
    if bilet == 'Finish' or movie == 'Finish':
        print(f"Total tickets: {total_total}")
        print(f"{percent_student:.2f}% student tickets.")
        print(f"{percent_standart:.2f}% standard tickets.")
        print(f"{percent_kid:.2f}% kids tickets.")
        break
    places = int(input())
    for i in range(1,places + 1):
        bilet = input()
        if bilet == 'student':
            count_student += 1
            count_student_total += 1
        if bilet == 'standart':
            count_standart += 1
            count_standart_total += 1
        if bilet == 'kid':
            count_kid += 1
            count_kid_total += 1
        total_tickets = count_student + count_standart + count_kid

        if bilet == 'End' or places < total_tickets:
            percent_full = (total_tickets / places) * 100
            total_total += total_tickets
            percent_student = count_student_total / total_total * 100
            percent_standart = count_standart_total / total_total * 100
            percent_kid = count_kid_total / total_total * 100
            print(f"{movie} - {percent_full:.2f}% full.")
            count_student = 0
            count_standart = 0
            count_kid = 0
            break


