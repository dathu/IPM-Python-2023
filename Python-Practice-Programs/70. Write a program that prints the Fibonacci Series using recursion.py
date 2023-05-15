def Fibonacci(i):
    if (i == 1):
        return 0 # In fibonacci series first term is always 0
    elif (i == 2):
        return 1
    return (Fibonacci(i - 1) + Fibonacci(i - 2))

no = int(input("Enter number upto which you want to print Fibonacci Series: "))
for i in range(1, no + 1):
    print(Fibonacci(i), end=" ")