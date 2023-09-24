period = int(input())
doctors = 7
treated = 0
untreated = 0
untreated_day = 0
treated_day = 0
for days in range(1, period + 1):
    cunsomers = int(input())
    if cunsomers > doctors:
        untreated_day = abs(cunsomers - doctors)
        untreated += untreated_day
    if cunsomers <= doctors:
        treated_day += cunsomers
    else:
        treated_day = cunsomers - untreated_day

    treated += treated_day
    if days % 3 == 0:
        if doctors < cunsomers:
            doctors += 1
            untreated -= 1
            treated += 1

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
