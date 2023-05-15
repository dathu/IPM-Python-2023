'''
Pattern#1
                            *
                        *   *   *
                    *   *   *   *   *
                *   *   *   *   *   *   *
            *   *   *   *   *   *   *   *   *


k = 1
i = 1
while i <= 5:
    space = 4
    while space >= i:
        print(' ', end=' ')
        space -= 1
    j = 1
    while j <= k:
        print('*', end=' ')
        j += 1
    print()
    k += 2
    i += 1
'''


'''
Pattern#2
                        *  *  *  *  *  *  *  *  *
                           *  *  *  *  *  *  *
                              *  *  *  *  *
                                 *  *  *
                                    *


k = 1
i = 1
while i <= 5:
    space = 1
    while space < i:
        print(' ', end=' ')
        space += 1
    j = 9
    while j >= k:
        print('*', end=' ')
        j -= 1
    print()
    k += 2
    i += 1
'''


'''
Pattern#3:
                            1   
                        1   2   3
                    1   2   3   4   5
                1   2   3   4   5   6   7
            1   2   3   4   5   6   7   8   9


k = 1
i = 1
while i <= 5:
    space = 4
    while space >= i:
        print(' ', end=' ')
        space -= 1
    j = 1
    while j <= k:
        print(j, end=' ')
        j += 1
    print()
    k += 2
    i += 1
'''


'''
Pattern#4:
                            1
                        2   2   2
                    3   3   3   3   3
                4   4   4   4   4   4   4
            5   5   5   5   5   5   5   5   5


k = 1
i = 1
while i <= 5:
    space = 4
    while space >= i:
        print(' ', end=' ')
        space -= 1
    j = 1
    while j <= k:
        print(i, end=' ')
        j += 1
    print()
    k += 2
    i += 1
'''


'''
Pattern#5:
                            1
                        3   3   3
                    5   5   5   5   5
                7   7   7   7   7   7   7
            9   9   9   9   9   9   9   9   9


k = 1
i = 1
while i <= 5:
    space = 4
    while space >= i:
        print(' ', end=' ')
        space -= 1
    j = 1
    while j <= k:
        print(k, end=' ')
        j += 1
    print()
    k += 2
    i += 1
'''