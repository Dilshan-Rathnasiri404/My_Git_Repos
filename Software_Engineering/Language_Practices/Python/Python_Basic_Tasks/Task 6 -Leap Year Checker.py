# Task 6 - Leap Year Checker

try:
    year = int(input('Enter a year: '))

    # Check if the year is divisible by 4
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
        
except ValueError:
    print("Invalid input! Please enter a valid numeric year.")
