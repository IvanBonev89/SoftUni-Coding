book_search = input()
numbers = 0
book = str(input())
while book != 'No More Books':
    if book == book_search:
        print(f"You checked {numbers} books and found it.")
        break
    if book != book_search:
        book = input()
        numbers += 1
        continue
else:
    print('The book you search is not here!')
    print(f"You checked {numbers} books.")

