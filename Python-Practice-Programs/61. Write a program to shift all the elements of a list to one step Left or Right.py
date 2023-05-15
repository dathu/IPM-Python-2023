'''
List = [5, 10, 15, 20, 25]

After shifting elements to the Left:
List = [10, 15, 20, 25, 5]

After shifting elements to the Right:
List = [25, 5, 10, 15, 20]
'''


emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    emptyList.append(values)
print(emptyList)

# For Left Shift:
# key = emptyList[0]
# for i in range(1, sizeOfList):
#     emptyList[i - 1] = emptyList[i]
# emptyList[sizeOfList - 1] = key
# print('List after shifting all the elements to one step Left =', emptyList)



# For Right Shift:
# key = emptyList[sizeOfList - 1]
# for i in range(sizeOfList - 2, -1, -1):
#     emptyList[i + 1] = emptyList[i]
# emptyList[0] = key
# print('List after shifting all the elements to one step Right =', emptyList)