"""
First Pattern:
*
* *
* * *
* * * *
* * * * *

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=" ")
        j += 1
    print()
    i += 1
"""

"""

Second Pattern:
* * * * *
* * * *
* * *
* *
*

i = 1
while i <= 5:
    j = 5
    while j >= i:
        print('*', end=" ")
        j -= 1
    print()
    i += 1
"""

"""
Third Pattern:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1
"""

"""

Fourth Pattern:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
"""

