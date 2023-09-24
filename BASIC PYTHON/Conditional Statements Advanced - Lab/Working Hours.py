# read user input
hours = int(input())
day = input()

# logic
if day in ('Monday Tuesday Wednesday Thursday Friday Saturday') and 10 <= hours <= 18:
    print('open')
else:
    print('closed')
