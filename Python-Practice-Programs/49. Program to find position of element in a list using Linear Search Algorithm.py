def LinearSearch(emptyList, sizeOfList, searchValue):
    flag = 0
    for i in range(sizeOfList):
        if emptyList[i] == searchValue:
            flag = 1
            position = i
    if flag == 1:
        print(f'The value you want to search in a list is at {position + 1} position.')
    else:
        print('Value not found!')


# Driver Code/main section
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list: '))
    emptyList.append(value)
print(emptyList)
searchValue = int(input('Enter value you want to search in a list: '))
LinearSearch(emptyList, sizeOfList, searchValue)