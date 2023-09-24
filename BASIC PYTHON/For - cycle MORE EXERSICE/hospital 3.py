period = int(input())

untreated = 0
treated = 0
doctors = 7

for days in range(1, period + 1):
    patients = int(input())
    if days % 3 == 0 and treated < untreated:
        doctors += 1
    if patients == doctors:
        treated += doctors
    elif patients < doctors:
        treated += patients
    else:
        treated += doctors
        untreated += (patients - doctors)

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
