lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('List is', lst)

# To find maximum number from a list.
# # First logic.
# max = lst[0]
# for i in lst:
#     if i > max:
#         max = lst[i]
# print('Maximum number in a list is', max)

# Second Logic:

# max = lst[0]
# for i in range(sizeOfList):
#     if lst[i] > max:
#         max = lst[i]
# print('Maximum number in a list is', max) 


# To find minimum number from a list.
min = lst[0]
for i in lst:
    if (min > i):
        min = lst[i]
print('Minimum number in the list is', min)