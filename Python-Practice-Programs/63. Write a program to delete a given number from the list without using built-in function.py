'''
lst = [5, 10, 15, 20, 25]

List after deleting 10 is:
lst = [5, 15, 20, 25]
'''

# This program is used to delete first occurence of a deleting element.

emptyList = []
sizeOfList = int(input('Enter size of the List: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a List: '))
    emptyList.append(values)
print('Original List =',emptyList)
deleteValue = int(input('Enter value which you want to delete from a list: '))
flag = 0
for i in range(sizeOfList):
    if(emptyList[i] == deleteValue):
        flag = 1
        position = i
        break
if(flag == 0):
    print('The element which you want to delete from a list is not in the list!')
else:
    for i in range(position, sizeOfList - 1):
        emptyList[i] = emptyList[i + 1]
    # emptyList.pop() # It deletes last element of a list.
    emptyList.pop(sizeOfList - 1) # you can use this logic as well.
print('List after deleting', deleteValue, 'from a list =', emptyList)
    