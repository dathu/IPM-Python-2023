no1 = int(input('Enter 1st number: '))
no2 = int(input('Enter 2nd number: '))
operation = input('Enter which operation would you like to perform? ')

if operation == '+':
    print(no1 + no2)
elif operation == '-':
    print(no1 - no2)
elif operation == 'x':
    print(no1 * no2)
elif operation == '/':
    print(no1 / no2)
else:
    print('You enter an invalid operator!')