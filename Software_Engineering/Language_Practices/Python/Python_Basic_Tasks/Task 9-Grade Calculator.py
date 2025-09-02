# Task 9 - Grade Calculator
print('- Grade Calculator -')

try:
    # Input marks for three subjects
    subject_1 = float(input('Input marks for Subject 1: '))
    subject_2 = float(input('Input marks for Subject 2: '))
    subject_3 = float(input('Input marks for Subject 3: '))

    # Validate marks
    if not (0 <= subject_1 <= 100) or not (0 <= subject_2 <= 100) or not (0 <= subject_3 <= 100):
        print('Error! Marks must be between 0 and 100.')
    else:
        # Calculate average
        average = (subject_1 + subject_2 + subject_3) / 3
        average = round(average, 2)

        # Determine grade
        if average >= 90:
            grade = 'A'
        elif 80 <= average < 90:
            grade = 'B'
        elif 70 <= average < 80:
            grade = 'C'
        elif 60 <= average < 70:
            grade = 'D'
        else:
            grade = 'F'

        # Display result
        print(f'Your average marks: {average}')
        print(f'Your Grade: {grade}')

except ValueError:
    print('Error! Please enter valid numeric marks.')
