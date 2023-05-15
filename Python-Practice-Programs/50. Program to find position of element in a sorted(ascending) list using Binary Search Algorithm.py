def BinarySearch(emptyList, sizeOfList, searchValue):
    i = 0
    j = (len(emptyList)) - 1
    flag = 0
    while (i <= j and flag == 0):
        mid = (i + j) // 2
        if (emptyList[mid] == searchValue):
            print('Value found!')
            position = mid
            flag = 1
        elif (emptyList[mid] > searchValue):
            j = mid - 1
        elif (emptyList[mid] < searchValue):
            i = mid + 1
    if flag == 1:
        print(f'The value you want to search in a list is at {position + 1} position.')
    else:
        print('Value not found!')
        

# Driver Code/main section
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list in ascending order: '))
    emptyList.append(value)
print(emptyList)
searchValue = int(input('Enter value you want to search in a list: '))
BinarySearch(emptyList, sizeOfList, searchValue)