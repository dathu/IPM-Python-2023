lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('List is', lst)

# 1st method.
# minValue = min(lst)
# maxValue = max(lst)
# print('Minimum number in the list is', minValue, 'and maximum number in the list is', maxValue)
# lst.remove(minValue)
# lst.remove(maxValue)
# secondMinvalue = min(lst)
# secondMaxvalue = max(lst)
# print('Second minimum number in the list is', secondMinvalue, 'and second maximum number in the ' 
#     'list is', secondMaxvalue)


# Find minimum/maximum and second minimum/maximum number in the list.
lst.sort()
print('Minimum Number =', lst[0], 'and maximum number is =', lst[-1])
print('Second Minimum Number =', lst[1], 'and second maximum number in the list is =', lst[-2])

# for max you can also write sizeOfList - 1
# for second max value you can also write sizeOfList - 2