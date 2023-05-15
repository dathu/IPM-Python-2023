"""
Short Description:

If user enters 10 for the value of n than only even numbers between 1 to 10 should be printed.
"""

# 1st method:
# n = int(input('Enter Number upto which you want to print: '))
# i = 2 # initialize the loop with i = 2 because we want to print only even numbers. 
# while i <= n: # because we want to print 10 also if n = 10 so thats why = is with < sign.
#     print(i)
#     i += 2
    
# 2nd Method:
n = int(input('Enter Number upto which you want to print: '))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1 # this increament is independent of the if block means this increament executes every time.

