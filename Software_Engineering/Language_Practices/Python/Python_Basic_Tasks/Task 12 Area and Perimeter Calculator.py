#12

print('-Area and Perimeter Calculator-')
print()

try:
    choice=input('Rectangle or Circle? Input "R" or "C" :')

    if choice == 'R':
        print(f'You prefer Rectangle. Press Enter')
        print()
        width=float(input('width (cm)= '))
        length=float(input('length (cm)= '))

        area = width*length
        area=round(area,2)
        perimeter = (2*width)+(2*length)
        perimeter = round(perimeter,2)

        print(f'area = {area}sqcm')
        print(f'perimeter = {perimeter}cm')


    elif choice == 'C' :
        print(f'You prefer Circle. Press Enter')
        print()
        radius=float(input('radius (cm)= '))

        
        area=(22/7)*(radius**2)
        area=round(area,2)
        perimeter=2*(22/7)*radius
        perimeter = round(perimeter,2)
        print(f'area= {area}sqcm')
        print(f'perimeter = {perimeter}cm')

    else:
        print('Error!Invalid input.')

        

except ValueError:
    print('Error! Value Error.')
