'''
Description:
Same like program # 39
'''

n = int(input('Enter number of rows: '))
i = 1
while n > 0:
    space = 1
    while space < i:
        print(' ', end=' ')
        space += 1
    j = 1
    while j <= ((n * 2) - 1):
        print('*', end=' ')
        j += 1
    print()
    n -= 1
    i += 1