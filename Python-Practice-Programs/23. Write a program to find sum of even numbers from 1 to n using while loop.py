# Method#1:
# n = int(input('Enter Number upto which you want to sum: '))
# i = 2
# sum = 0
# while i <= n:
#     sum += i
#     i += 2
# print('The Sum of Even numbers between 1 and',n,'is =', sum)



# Method#2:
n = int(input('Enter Number upto which you want to sum: '))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print('The Sum of Even numbers between 1 and',n,'is =', sum)

