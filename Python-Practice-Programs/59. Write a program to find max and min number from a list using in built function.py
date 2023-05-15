lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('List is', lst)
maxValue = max(lst)
minValue = min(lst)
print('Maximum number of the list is', maxValue)
print('Minimum number of the list is', minValue)