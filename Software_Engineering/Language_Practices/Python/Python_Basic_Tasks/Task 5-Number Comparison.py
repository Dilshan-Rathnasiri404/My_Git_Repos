print("-Number Comparison-")

try:
    first_number=int(input('Enter a number :'))
    second_number=int(input('Enter another number :'))

    if first_number > second_number:
        print('First number is greater')

    elif first_number < second_number:
        print('Second number is greater')

    else:
        print('Both numbers are equal')

except ValueError:
    print('Error! Invalid input!')
    
