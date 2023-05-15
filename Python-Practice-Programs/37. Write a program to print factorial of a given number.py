"""
Description:
factorial is a concept in mathematics it is basically like if we say find factorial of 5 then
5 x 4 x 3 x 2 x 1 = 120, so 120 is the factorial of 5.
"""

no = int(input('Enter Number to find its factorial: '))
originalNo = no
factorial = 1
while no > 0:
    factorial = factorial * no
    no -= 1
print('Factorial of',originalNo,'is =',factorial)