"""
Description:

lets say if a user enters 5 for the value of n so it means the program calculates the sum of numbers from
1 till 5.
like 1 + 2 + 3 + 4 + 5 = 15. so the sum of the numbers from 1 till 5 is equal to 15.
"""

n = int(input('Enter Number upto which you want to sum: '))
i = 1
sum = 0 # Here we set sum = 0 because zero is the number that does'nt effect the sum of two numbers like
# if we add 1 + 0 then answer is 1 so it means 0 does'nt effect the sum.
while i <= n:
    sum += i
    i += 1
print('The sum =', sum)
