"""
Description:
This program simply prints the table of a number that you entered.
"""

no = int(input('Enter Number: '))
i = 1
while i <= 12:
    print(f'{no} x {i} =', no * i)
    i += 1