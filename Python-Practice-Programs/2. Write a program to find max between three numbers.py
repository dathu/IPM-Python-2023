no1 = int(input('Enter 1st number: '))
no2 = int(input('Enter 2nd number: '))
no3 = int(input('Enter 3rd number: '))

if no1 > no2 and no1 > no3:
    print('Max number is', no1)

elif no2 > no1 and no2 > no3:
    print('Max number is', no2)

else:
    print('Max number is', no3)

"""Here and operator is used because in order to find max between 3 numbers both the conditions around a
logical operator must be true"""