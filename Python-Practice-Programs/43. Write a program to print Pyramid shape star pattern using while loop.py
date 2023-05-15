'''
Description:
Same like program # 39
'''

k = 1
i = 1
while i <= 5:
    space = 1
    while space <= 5 - i:
        print(' ', end=' ')
        space += 1
    j = 1
    while j <= k:
        print('*', end=' ')
        j += 1
    k += 2
    print()
    i += 1