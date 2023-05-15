"""
Description:
Reverse means if the user enters 287 then the output is 782.
"""

no = int(input('Enter Number to find its reverse: '))
rev = 0
while no > 0:
    rev = (rev * 10) + (no % 10)
    no = no // 10
print('The Reverse of a number is =', rev)