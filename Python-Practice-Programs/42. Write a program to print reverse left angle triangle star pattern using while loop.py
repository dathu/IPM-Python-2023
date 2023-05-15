'''
Description:
Same like program # 42.
'''

i = 1
while i <= 5:
    space = 1
    while space < i:
        print(' ', end=' ')
        space += 1
    j = 5
    while j >= i:
        print('*', end=' ')
        j -= 1
    print()
    i += 1