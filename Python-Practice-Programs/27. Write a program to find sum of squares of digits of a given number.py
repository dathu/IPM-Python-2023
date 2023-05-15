"""Description:
.) Same as program#25
"""

no = int(input('Enter Number to find sum of squares of digits of a number: '))
sum = 0
while no > 0:
    sum += ((no % 10) ** 2)
    no //= 10
print('The sum of square of each digit =', sum)
