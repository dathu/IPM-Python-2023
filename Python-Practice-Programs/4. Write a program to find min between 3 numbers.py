no1 = int(input('Enter 1st number: '))
no2 = int(input('Enter 2nd number: '))
no3 = int(input('Enter 3rd number: '))

if no1 < no2 and no1 < no3:
    print('Min number is', no1)

elif no2 < no1 and no2 < no3:
    print('Min number is', no2)

else:
    print('Min number is', no3)