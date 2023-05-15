def DeleteValue(emptyList, sizeOfList, deleteValue):
    # if in case list is not sorted then first .sort() method apply on a list and then insert value in it.
    # when array is sorted so implementing binary search is a better option to find the position of
    # a value.
    i = 0
    j = (len(emptyList)) - 1
    flag = 0
    while (i <= j and flag == 0):
        mid = (i + j) // 2
        # for descending order list both conditions are reversed.
        if emptyList[mid] == deleteValue:
            position = mid
            flag = 1
        elif emptyList[mid] > deleteValue:
            j = mid - 1
        elif emptyList[mid] < deleteValue:
            i = mid + 1
    if flag == 1:
        return position
    else:
        return -1 # -1 means value not found.
    
    
    
# Driver code/main section
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list in ascending order: '))
    emptyList.append(value)
print(f'List before deletion of a desired element is:', emptyList)
deleteValue = int(input('Enter value which you want to delete from a list: '))
deletionFunction = DeleteValue(emptyList, sizeOfList, deleteValue)
if deletionFunction == -1:
    print('The value you want to delete from a list is not present in the list.')
else:
    del(emptyList[deletionFunction])
    print('List after deletion is', emptyList)