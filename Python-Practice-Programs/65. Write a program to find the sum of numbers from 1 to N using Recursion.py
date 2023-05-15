'''
If n = 4 then 1 + 2 + 3 + 4 = 10
we start our program from 4 to 1
4 => Recursion start from 4
3
2
1 => This is the base case of this program so recursion stops here.
'''


def Sum(n):
    if n == 1:
        return 1
    else:
        return (n + Sum(n - 1))

n = int(input("Enter number upto which you want to sum: "))
sum = Sum(n)
print(f"Sum of numbers from {1} to {n} is {sum}")
