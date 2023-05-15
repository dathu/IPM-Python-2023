# In this program we write a logic that reverse a list itself.
'''
List stores different types of elements in it.
Array stores similar types of elements in it.
In this program we stores int into a list that's why it becomes array.
'''

lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('Original list is =', lst)

i = 0
j = sizeOfList - 1
while(i < j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    i += 1
    j -= 1
print('List aftre reverse =', lst)

# for i in range(sizeOfList):
#     print(lst[i])

# for i in lst:
#     print(i)