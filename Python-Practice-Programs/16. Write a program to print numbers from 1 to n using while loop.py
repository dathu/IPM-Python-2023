# n = int(input('Enter Number upto which you want to print: '))
# i = 1
# if n > 0:
#     while i <= n:
#         print(i)
#         i+=1
# # the final value of i is 6 but it will not print because the condition becomes false when i = 6.
# else:
#     print('You entered negative number that\'s why program does\'nt print numbers')



"""
This is the second logic of the same problem problem which we solved above.
"""

i = int(input('Enter the initization number: '))
n = int(input('Enter Number upto which you want to print: '))
if n > 0:
    while i <= n:
        print(i, end=" ")
        i+=1
# the final value of i is 6 but it will not print because the condition becomes false when i = 6.
else:
    print('You entered negative number that\'s why program does\'nt print numbers')