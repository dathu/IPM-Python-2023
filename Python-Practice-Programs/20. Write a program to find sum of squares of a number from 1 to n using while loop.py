n = int(input('Enter a number upto which you want to sum: '))
i = 1
sum = 0
while i <= n:
    sum += i**2 # or you can write sum += i*i
    i += 1
print('The sum of squares =', sum)