"""
Description:

sum of n even numbers means if n = 4 then it can add 2 + 4 + 6 + 8 and if n = 5 then 10 also added.
n = 4 means first 4 even numbers.
if n = 4 then the sum = 20.
Here n will be decided by the user.

n = 3 then 2 + 4 + 6 = 12
"""

n = int(input('How many even numbers you want to add: '))
i = 1 # here if we initialize i with 2 then its also works fine.
sum = 0
count = 0 # it can count the values like if user want to sum of first 3 even numbers then this var count
# the value.
while count < n: # here we dont write count <= n because if we add = to the condition than it can count
# like if n = 3 then it can count 4 values but we have count first 3 even numbers that's why we didn't write
# = to the condition.
# if count starting from 1 then in this case we write count <= n.
    if i % 2 == 0:
        sum += i
        count += 1
    i += 1
print('The sum of first', count, 'even numbers =', sum)