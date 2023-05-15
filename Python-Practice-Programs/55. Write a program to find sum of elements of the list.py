lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('List is', lst)

# 1st logic.

# sum = 0
# for i in lst:
#     sum += i
# print('Sum of elements of the list is', sum)


# 2nd logic.

sum = 0
for i in range(sizeOfList):
    sum += lst[i]
# print('Sum of elements of the list is', sum)