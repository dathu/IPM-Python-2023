"""
Description:
Palindrome numbers are those numbers in which if we find the reverse of number and the reverse is same as
that of original number then the number is palindrome number.
lets say if we choose 525 then the reverse of this number is also 525 then 525 is a palindrome number.
"""

no = int(input('Enter Number to check whether it is palindrome or not: '))
originalNo = no
rev = 0
while no > 0:
    rev = (rev * 10) + (no % 10)
    no = no // 10
if originalNo == rev:
    print('The Number is a palindrome number.')
else:
    print('The Number is not a palindrome number.')