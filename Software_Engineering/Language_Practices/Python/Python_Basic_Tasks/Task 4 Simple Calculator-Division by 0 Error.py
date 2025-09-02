try:
    first_number = float(input('Enter a number :'))
    operation=input('Enter the operation :')
    second_number=float(input('Enter a number :'))


    if operation == '+': 
         print('Answer= ', first_number + second_number)
        
    elif operation== '-' :
         print('Answer= ', first_number - second_number)
   
    elif operation== '*' :
         print('Answer= ', first_number * second_number)

    elif operation== '/' :
        if second_number==0 :
            print('Error! Division by 0 is not allowed:')

        else:
            print('Answer= ', first_number / second_number)
 
except ValueError:
            print('Invalid Input!')
