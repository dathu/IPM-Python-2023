"""Description:
.) Same as program#27
"""

no = int(input('Enter Number to find sum of cubes of digits of a number: '))
sum = 0
while no > 0:
    sum += ((no % 10) ** 3)
    no //= 10
print('The sum of cube of each digit =', sum)
