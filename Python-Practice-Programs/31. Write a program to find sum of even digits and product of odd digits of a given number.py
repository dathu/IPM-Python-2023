"""
Description:

Core logic is same as program#25.

In this program if we enter a number like 2345 so the program will calculate the sum of
even numbers exist in the digit like in this case 2 and 4 are present as a even number in 2345
so it means the sum = 2 + 4 = 6
same the program will also calculate the product of odd numbers exist in the digit like in this case
3 and 5 means the product = 3 * 5 = 15.
"""

no = int(input('Enter Number: '))
sum = 0
product = 1
while no > 0:
    d = no % 10
    if d % 2 == 0:
        sum = sum + d
    else:
        product = product * d
    no = no // 10
print('The sum of even digits =', sum, 'and the product of odd digits =', product)