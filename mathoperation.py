# importing "math" for mathematical operations 
import math


# using square root(sqrt) function contained 
# in math module
x=25
print ("square root of x = ",math.sqrt(x))
print("\n")
print("-------------------------------------------")
#-------------------------------------------

# using pi function contained in math module 
print ("Value of PI = ",math.pi) 
print("\n")
print("-------------------------------------------")

#-------------------------------------------


# 2 radians = 114.59 degreees 
print ("Value of 2 radians = ",math.degrees(2))
print("\n")
print("-------------------------------------------")

#-------------------------------------------

# 60 degrees = 1.04 radians 
print ("Value of 60 degrees =",math.radians(60)) 
print("\n")
print("-------------------------------------------")

#-------------------------------------------

# Sine of 2 radians 
print ("Value of Sine of 2 radians =",math.sin(2))
print("\n")
print("-------------------------------------------")

#-------------------------------------------

# Cosine of 0.5 radians 
print ("Cosine of 0.5 radians=",math.cos(0.5)) 
print("\n")
print("-------------------------------------------")

#-------------------------------------------
#------------------------------------------
# Tangent of 0.23 radians 
print ("Tangent of 0.23 radians = ",math.tan(0.23))
print("\n")
#-------------------------------------------

# 1 * 2 * 3 * 4 = 24 
print ("Factorial of 4 =",math.factorial(4))
print("\n")
print("-------------------------------------------")
#-------------------------------------------

# Python code to demonstrate the working of ceil() and floor() 

a = 2.3

# returning the ceil of 2.3 
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
print("\n")
print("-------------------------------------------")
#-------------------------------------------

# returning the floor of 2.3 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a)) 
print("\n")
print("-------------------------------------------")
#-------------------------------------------

a = -10
  
b= 5
  
# returning the absolute value. 
print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a))
print("\n")
print("-------------------------------------------")
#-------------------------------------------
  
# returning the factorial of 5 
print ("The factorial of 5 is : ", end="") 
print (math.factorial(b))
print("\n")
print("-------------------------------------------")
#-------------------------------------------


a = -10
b = 5.5
c = 15
d = 5

 #copysign(a, b) :This function returns the number with the value of ‘a’ but with the sign of ‘b’.
 #The returned value is float type. returning the copysigned value. 
print ("The copysigned value of -10 and 5.5 is : ") #, end=""
print (math.copysign(5.5, -10))
print("\n")
print("-------------------------------------------")
#-------------------------------------------
  
# returning the gcd of 15 and 5 
print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(5,15)) 
print("\n")
print("-------------------------------------------")
#-----------------------------------------------------

# importing built in module random 
import random 
  
# printing random integer between 0 and 5
print("printing random integer between 0 and 5 = ", end="") 
print (random.randint(0, 5))  
print("\n")
print("-------------------------------------------")
#-----------------------------------------------------

# print random floating point number between 0 and 1
print("printing random floating point number between 0 and 1 = ", end="") 
print (random.random())  
print("\n")
print("-------------------------------------------")
#-----------------------------------------------------

# random number between 0 and 100
print("random number between 0 and 100 = ", end="")
print (random.random() * 100)
print("\n")
print("-------------------------------------------")
#-----------------------------------------------------

List = [1, 4, True, 800, "python", 27, "hello"] 
  
# using choice function in random module for choosing a random element from a set such as a list
print("random element from a list = ", end="")
print (random.choice(List))
print("\n")
print("-------------------------------------------")
#-----------------------------------------------------
