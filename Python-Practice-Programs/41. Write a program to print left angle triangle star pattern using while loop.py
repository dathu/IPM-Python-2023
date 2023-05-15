"""
Same like program # 39
"""

i = 1
while i <= 5: # This loop will count the number of row's.
    space = 1
    while space <= 5 - i: # This loop will print the blank spaces.
        print(' ', end=' ')
        space = space + 1
    j = 1
    while j <= i: # This loop will print stars.
        print('*', end=' ')
        j = j + 1
    print()
    i = i + 1