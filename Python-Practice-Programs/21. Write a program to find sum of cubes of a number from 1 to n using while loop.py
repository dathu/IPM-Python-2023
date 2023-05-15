n = int(input('Enter a number upto which you want to sum: '))
sum = 0
i = 1
while i <= n:
    sum += i**3
    i += 1
print("The sum of cubes =", sum)