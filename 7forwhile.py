count = 0 
while (count < 9): 
    print ('The count is:', count)
    count = count + 1

#---------------------------------------------------
for i in range(3): 
	print(i)

#----------------------------------------------------
for i in range(1,6): 
	print(i)

#----------------------------------------------------
for i in range(2,10,2) :
	print(i)

#----------------------------------------------------
# Python program to illustrate Iterating over a String
print("\nString Iteration")
for letter in 'Python' :
	print ('Current Letter :', letter)

#----------------------------------------------------
# Python program to illustrate Iterating over a list
print("\nList Iteration")
fruits = ['banana', 'apple', 'mango'] 
for fruit in fruits:
	print ('Current fruit :', fruit)

#-----------------------------------------------------
# Python program to illustrate Iterating over a tuple (immutable)
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i)
#-----------------------------------------------------  
#Python program to illustrate Iterating over dictionary 
print("\nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s  %d" %(i, d[i]))
#--------------------------------------------------------
# Python program to illustrate Iterating by index 
print("\nIterating by index ")
list = ["gmit", "jnnce", "ece"] 
for index in range(len(list)): 
	print (list[index])
print("\n")
#--------------------------------------------------------
                #Loop Control Statements
#-------------------------------------------------------
# 1. Continue Statement: It returns the control to the beginning of the loop.
	
# Prints all letters except 'e' and 's' 
for letter in 'davangereshimogga':  
    if letter == 'a' or letter == 'g': 
         continue
    print ('Current Letter :', letter)
    #var = 10
#--------------------------------------------------------
# 2. Break Statement: It brings control out of the loop

for letter in 'davangereshimogga': 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'a' or letter == 'g': 
		break

print ('Current Letter :', letter) 
#--------------------------------------------------------
# 3. Pass Statement: We use pass statement to write empty loops.
#Pass is also used for empty control statement, function and classes.

# An empty loop 
for letter in 'davangereshimogga': 
	pass
print ('Last Letter :', letter )
#-----------------------------------------------------------
