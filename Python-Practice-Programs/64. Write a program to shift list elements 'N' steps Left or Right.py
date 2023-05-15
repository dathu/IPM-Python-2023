emptyList = []
sizeOfList = int(input('Enter size of the List: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a List: '))
    emptyList.append(values)
print('Original List =',emptyList)
shiftValue = int(input("Enter No of position you want to shift in Left/Right: "))

# For N steps right shift:
for count in range(shiftValue):
    storeValue = emptyList[sizeOfList - 1]
    for i in range(sizeOfList - 2, -1, -1):
        emptyList[i + 1] = emptyList[i]
    emptyList[0] = storeValue
print(f"List after shifting elements to {shiftValue} steps right is {emptyList}")


# For N steps left shift
'''
for count in range(shiftValue):
    storeValue = emptyList[0]
    for i in range(1, sizeOfList):
        emptyList[i - 1] = emptyList[i]
    emptyList[sizeOfList - 1] = storeValue
print(f"List after shifting elements to {shiftValue} steps left is {emptyList}")
'''