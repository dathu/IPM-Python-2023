"""
Description:

This is the same program as program#24. In this program we print first n even numbers like
if n = 3 then the program prints 2,4,6
"""

n = int(input('How many even numbers from starting you want to print? '))
i = 1
count = 0
while count < n:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1