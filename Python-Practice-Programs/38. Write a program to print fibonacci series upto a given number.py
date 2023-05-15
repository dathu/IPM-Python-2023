"""
Description:
Fibonacci Series is a concept in mathematics like it is the series in which the elements are like:
0 1 1 2 3 5 8 13 and so on.
In this series it is shown that:
0 + 1 = 1
and 1 + 1(previous number) = 2
2 + 1(previous number) = 3
3 + 2(previous number) = 5
5 + 3(previous number) = 8
8 + 5(previous number) = 13
and the series goes on like this...
"""

no = int(input('Enter Number upto which you want to print fibonacci series: '))
x = 0
y = 1
z = 0
while z <= no:
    print(z, end=" ")
    x = y
    y = z
    z = x + y