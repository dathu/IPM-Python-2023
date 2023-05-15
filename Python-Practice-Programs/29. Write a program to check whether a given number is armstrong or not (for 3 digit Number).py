"""
Description:

Armstrong numbers are those in which we find sum of cubes of each digit of a number and
in the armstrong number case lets say if user enters a number 153 so
1***3 + 5***3 + 3***3
1 + 125 + 27 = 153, so as we see the sum number returns even after we calculate sum of cubes of
each digit of a number so it means 153 is an armstrong number.

"""

no = int(input('Enter Number to check whether it is armstrong or not: '))
orginalNumber = no
sum = 0
while no > 0:
    sum = sum + ((no % 10) ** 3)
    no = no // 10
if sum == orginalNumber:
    print('The Number is armstrong.')
else:
    print('The number is not armstrong.')
