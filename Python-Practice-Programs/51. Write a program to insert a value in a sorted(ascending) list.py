def InsertValue(emptyList, sizeOfList, insertValue):
    # if in case list is not sorted then first .sort() method apply on a list and then insert value in it.
    i = (len(emptyList)) - 1
    emptyList[i + 1] = emptyList.append(None)
    while (emptyList[i] > insertValue and i >= 0):
        emptyList[i + 1] = emptyList[i]
        i -= 1
    emptyList[i + 1] = insertValue
    print(f'List after inserting {insertValue} to its suitable index is {emptyList}')


# Driver Code/main section
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list in ascending order: '))
    emptyList.append(value)
print(f'List before inserting a value is {emptyList}')
insertValue = int(input('Enter value you want to insert in a list: '))
InsertValue(emptyList, sizeOfList, insertValue)