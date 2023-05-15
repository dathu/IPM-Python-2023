def Reverse(s, n):
    if n == 0:
        print(s[0])
    else:
        print(s[n], end='')
        Reverse(s, n - 1)

s = input("Enter String to find its reverse: ")
Reverse(s, len(s) - 1)