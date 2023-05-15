'''
*
* *
* * *
* * * *
* * * * *

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1
'''

'''
* * * * *
* * * *
* * *
* *
*

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*', end=' ')
        j -= 1
    print()
    i += 1
'''

'''
        *
      * *
    * * *
  * * * *
* * * * *


i = 1
while i <= 5:
  space = 4
  while space >= i:
    print(' ', end=' ')
    space -= 1
  j = 1
  while j <= i:
    print('*', end=' ')
    j += 1
  print()
  i += 1
'''

'''
* * * * *
  * * * *
    * * *
      * *
        *


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
'''

'''
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