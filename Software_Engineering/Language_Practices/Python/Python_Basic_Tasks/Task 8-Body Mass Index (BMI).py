#Task 8

print('-Body Mass Index (BMI)-')

try:
    weight=float(input('Input your weight in kilograms : '))
    height=float(input('Input your height in meters : '))

    if weight <= 0 or height <= 0:
        print('Error! weight and height must be positive numbers.')

    else:
        BMI=weight/(height**2)
        BMI=round(BMI,2)

        if BMI<18.5 :
            print(f'Your BMI value is {BMI} and that means you are underweight')

        elif 18.5 <= BMI < 24.9 :
            print(f'Your BMI value is {BMI} and that means your weight is normal.')

        elif 25 <= BMI < 29.9 :
            print(f'Your BMI value is {BMI} and that means you are Overweight')

        elif BMI >= 30 :
            print(f'Your BMI value is {BMI} and that means you are Obese.')

except ValueError:
    print('Error! Enter a valid numeric value!')
