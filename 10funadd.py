# A simple Python function to cadd 2 numbers 
# Function definition is here

print(" Sum of Two Numbers\n")
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print ("Outside the function : ", total)
print("---------------------------------")

#-------------------------------------------------------

# A simple Python function to check whether x is even or odd

print(" Even or Odd Function\n")

def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")
  
# Driver code 
evenOdd(2) 
evenOdd(3)
print("---------------------------------")

#-------------------------------------------------------

# Python program to demonstrate Keyword Argument pair.
#The idea is to allow caller to specify argument name with values so that
#caller does not need to remember order of parameters.

def student(firstname, lastname): 
	print(firstname, lastname) 
	
	
# Keyword arguments pair				 
student(firstname ='RavitejB', lastname ='Raghudathesh')	 
student(lastname ='Raghudathesh', firstname ='RavitejB') 


print("\n")
print("---------------------------------")

#-------------------------------------------------------
# Important program:- Python program to illustrate *args for variable number of arguments (imp) 
def myFun(*raghu): 
	for arg in raghu: 
		print (arg) 
	
myFun('Hello', 'Welcome', 'to', 'JNNCE' , 'SDP') 
print("\n")
myFun('We', 'are', 'from', 'GMIT')
print("\n")
print("---------------------------------")
#-------------------------------------------------------

# Important program:-  Python program to illustrate  *kargs for variable number of keyword arguments (imp) 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='gmit', mid ='to', last='jnnce')	 

print("\n")
print("---------------------------------")
#-------------------------------------------------------

#Anonymous functions: In Python, anonymous function means that a function is without a name.
#As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

# Python code to illustrate cube of a number using labmda function 
	
cube = lambda x: x*x*x 
print(cube(7)) 

print("---------------------------------")
#-------------------------------------------------------
