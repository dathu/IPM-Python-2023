emptyList = []
sizeOfList = int(input('Enter size of the List: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a List: '))
    emptyList.append(values)
print(emptyList)
insertValue = int(input('Enter value to insert in a List: '))
position = int(input('Enter Position at which you want to insert an element in a List: '))
emptyList.append(None)
for i in range(sizeOfList - 1, position - 2, -1):
    emptyList[i + 1] = emptyList[i]
emptyList[position - 1] = insertValue
print('List after inserting', insertValue, 'to the', position, 'position is =', emptyList)