def findBasetoThePower(x, y):
    if y == 0:
        return 1
    else:
        return (x * findBasetoThePower(x, y - 1))

x = int(input('Enter base: '))
y = int(input("Enter exponent: "))
result = findBasetoThePower(x, y)
print(f"{x} to the power {y} is {result}.")