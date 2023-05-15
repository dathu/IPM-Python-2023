"""
Description:

In this program we have to find sum of digits of a given number.
it means if the user enter 243 means the program calculates the sum of 2 + 4 + 3 = 9, so the if the user
enters 243 then sum = 9.
if user enters 248 as a value of n than we have to extract each value one by one like
first extract 8 then 4 and then 2.
248 % 10 = 8
24 % 10 = 4
2 % 10 = 0
below there in code we write no //= 10,here // is used because if we like use / this then
248 / 10 = 24.8 so this is a bit problamatic because at this point  we have to extract 4 after extracting
8 so for extracting 4 we use // then it gives us 24 and the process continues.
"""

no = int(input('Enter Number to find sum of digits: '))
sum = 0 # sum ko 0 pe set or multiplication ko 1 pe set.
while no > 0:
    sum += no % 10 # sum = sum + (no % 10)
    no //= 10 # no = no // 10
print('Sum of digits of a number =', sum)
