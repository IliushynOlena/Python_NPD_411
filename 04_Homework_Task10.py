day = 29
month = 2
year = 2024
print(f" {day}/{month}/{year}")
day += 1#32

fullDays = 0

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    fullDays = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    fullDays = 30
elif month == 2:
    if year %400 == 0 or (year %4 == 0 and year %100 != 0):
        fullDays = 29
    else:
        fullDays = 28

if day > fullDays:
    day = 1
    month +=1

if month > 12:
    month = 1
    year +=1

print(f" {day}/{month}/{year}")