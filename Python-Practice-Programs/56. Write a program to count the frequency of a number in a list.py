lst = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    values = int(input('Enter values to store in a list: '))
    lst.append(values)
print('List is', lst)

countValue = int(input('Enter no to find its frequency in a list: '))
count = 0
for i in lst:
    if i == countValue:
        count += 1
print(f'Frequency of {countValue} in the list is {count}')