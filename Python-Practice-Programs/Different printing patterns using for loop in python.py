'''
*
* *
* * *
* * * *
* * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
'''

'''
* * * * *
* * * *
* * *
* *
*
'''

'''
        *
      * *
    * * *
  * * * *
* * * * *

for i in range(1, 6):
    for j in range(4, i-1, -1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print('*', end=' ')
    print()
'''

'''
* * * * *
  * * * *
    * * *
      * *
        *

for i in range(1, 6):
    for j in range(1, i):
        print(' ', end=' ')
    for j in range(5, i-1, -1):
        print('*', end=' ')
    print()
'''