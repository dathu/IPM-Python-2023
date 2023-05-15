def removeDuplicate(lst):
    noDuplicateList = []
    for i in lst:
        if i not in noDuplicateList:
            noDuplicateList.append(i)
    return noDuplicateList
        
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list: '))
    emptyList.append(value)
print(emptyList)
lst = removeDuplicate(emptyList)
print('List after removing duplicate elements is',lst)