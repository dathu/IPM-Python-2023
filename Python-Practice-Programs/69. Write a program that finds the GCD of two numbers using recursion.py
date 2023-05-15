'''
What is GCD ?

The greatest common divisor (GCD), also called the greatest common factor, of two numbers is the largest 
number that divides them both. For instance, the greatest common factor of 20 and 15 is 5,since 5 divides
both 20 and 15 and no larger number has this property. 

'''

def GCD(no1, no2):
    if no2 == 0:
        return no1
    else:
        return (GCD(no2, no1 % no2))


no1 = int(input("Enter 1st no: "))
no2 = int(input("Enter 2nd no: "))
gcd = GCD(no1, no2)
print(f"GCD of {no1} and {no2} is {gcd}.")