#Task 11
#Temperature Converter
print('-Temperature Converter (Celcius to Fahrenheit and Vice versa)-')
print()

try:
    value=float(input('Enter Temperature = '))
    unit=input('Unit (C/F)= ')

    if unit== 'C' :
        temperature= (9/5)*value + 32
        temperature=round(temperature,2)
        print()
        print(f'Temperature = {temperature}F')

    elif unit== 'F':
        temperature=(value - 32)*(5/9)
        temperature=round(temperature,2)
        print()
        print(f'Temperature = {temperature}C')

    else:
        print('Error! Please enter the correct unit.')

except ValueError:
    print('Error! The Temperature Value you entered is not numeric.')
