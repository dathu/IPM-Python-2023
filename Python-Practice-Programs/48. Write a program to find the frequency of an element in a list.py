'''
Frequency means how many times the element repeated in list.
'''

emptyList = []
for i in range(5):
    no = int(input('Enter number to store in a list: '))
    emptyList.append(no)
findFrequency = int(input('Enter an element to find its frequency: '))
print('Frequency of',findFrequency,'is',emptyList.count(findFrequency))