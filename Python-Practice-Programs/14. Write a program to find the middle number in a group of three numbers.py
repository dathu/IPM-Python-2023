no1 = int(input('Enter 1st number: ')) # 5
no2 = int(input('Enter 2nd number: ')) # 4
no3 = int(input('Enter 3rd number: ')) # 6

"""
Description:

The logic in this question is that if we have 3 numbers like a,b and c so in this case if we say a is a
middle number then there is a two conditions. first is that a is greater than b and less than c.
the second condition is that a is less than b and greater than c. and in this case both conditions works
at the same time with the logical operator 'or'.
"""

if (no1 > no2 and no1 < no3) or (no1 > no3 and no1 < no2):
    print('Middle number is:', no1)
elif (no2 > no1 and no2 < no3) or (no2 > no3 and no2 < no1):
    print('Middle number is:', no2)
else:
    print('Middle number is:',no3)