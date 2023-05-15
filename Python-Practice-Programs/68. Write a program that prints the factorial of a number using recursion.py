'''
factorial, in mathematics, the product of all positive integers less than or equal to a given positive 
integer and denoted by that integer and an exclamation point. Thus, factorial seven is written 7!, 
meaning 1 x 2 x 3 x 4 x 5 x 6 x 7. Factorial zero is defined as equal to 1.
'''

def Factorial(no):
    if no == 1:
        return 1
    else:
        return (no * Factorial(no - 1))


no = int(input("Enter number to find its factorial: "))
factorial = Factorial(no)
print(f"Factorial of {no} is {factorial}.")