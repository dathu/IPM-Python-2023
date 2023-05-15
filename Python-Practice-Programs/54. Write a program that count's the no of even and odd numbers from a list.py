def countEvenOddNos(lst):
    countEvenNos = 0
    countOddNos = 0
    for i in lst:
        if (i % 2) == 0:
            countEvenNos += 1
        else:
            countOddNos += 1
    print('The total even no\'s in a list are', countEvenNos, 'and the total odd no\'s are', countOddNos)
    
    
emptyList = []
sizeOfList = int(input('Enter size of the list: '))
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list: '))
    emptyList.append(value)
print(emptyList)
countEvenOddNos(emptyList)