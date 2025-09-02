#Task 7

print('-Simple Interest Calculator-')

try:
    P=float(input('Principle amount = '))
    R=float(input('Annual interest rate in percentage = '))
    T=float(input('Time in years = '))


    simple_interest=(P*R*T)/100

    print(f'Interest = {simple_interest}')

except ValueError:
    print('Error! Input valid numeric values.')
