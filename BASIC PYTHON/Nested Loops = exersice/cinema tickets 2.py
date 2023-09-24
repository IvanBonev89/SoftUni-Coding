student_tickets = 0
standart_ticekts = 0
kid_tickets = 0
movie = input()
while movie != "Finish":
    free_seats = int(input())
    sold_seats = 0
    for free_ticket in range(free_seats):
        current_ticket = input()
        if current_ticket == 'End':
            break
        elif current_ticket == 'student':
            student_tickets += 1
        elif current_ticket == 'standard':
            standart_ticekts += 1
        elif current_ticket == 'kid':
            kid_tickets += 1
        sold_seats += 1
    percent_full = sold_seats / free_seats * 100
    print(f"{movie} - {percent_full:.2f}% full")
    movie = input()
total_sold = student_tickets + standart_ticekts + kid_tickets
percent_student = student_tickets / total_sold * 100
percent_standart = standart_ticekts / total_sold * 100
percent_kid = kid_tickets / total_sold * 100

print(f"Total tickets: {total_sold}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standart:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
