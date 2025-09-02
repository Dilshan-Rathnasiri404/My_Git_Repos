#Task 3

name=input('What is your name?')


try:
    age=int(input("How old are you? "))

    if age<=0:
        print("Invalid input. Age cannot be negative")

    else:
        years_to_century= 100 - age
        year= 2024 + years_to_century
        print(f'Hello, {name}! You will turn 100 years in the year {year}.')

except ValueError:
    print("Invalid input! Please enter a numeric value for age.")
    
