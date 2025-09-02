#Task 10
#Electricity Bill Calculator

print('-Electricity Bill Calculation-')
print()

try:
    Number_of_units_consumed=int(input('Enter number of units consumed = '))
    if (Number_of_units_consumed <= 0):
        print('Error! Invalid input the meter reading cannot be negative.')

    else:
        if (Number_of_units_consumed < 100) :
            charge= (Number_of_units_consumed * 5)

        elif (Number_of_units_consumed < 200):
            charge=(100*5)+((Number_of_units_consumed - 100)* 7)

        else : 
            charge=(100*5)+(100*7)+((Number_of_units_consumed - 200)*10)

        print(f'Total amount you have to pay = ₹ {charge}/=')

except ValueError:
    print('Error! Non-numeric or negative values are not valid')
    

        
