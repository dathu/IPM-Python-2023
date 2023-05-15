"""
Description:
The prime numbers are basically those numbers which are always divisible by 1 and itself.
divisible means reminder = 0.
like 13, 13 is divisible by 1 and 13 itself so it is prime because it was divisible by exactly two
no's but if we enter a number which was divisible from more than 2 numbers then it was a composite number
like 2,4,6 etc they are composite numbers.
"""

no = int(input('Enter Number to check whether it is prime or not: '))
count = 0
i = 1
while i <= no:
    if no % i == 0:
        count += 1
    i += 1
if count == 2:
    print('The Number is prime.')
else:
    print('The Number is a composite number.')