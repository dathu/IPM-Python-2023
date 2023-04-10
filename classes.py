# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:17:56 2019

@author: dathe
"""

 creates a class named MyClass 
class MyClass: 
		# assign the values to the MyClass attributes 
		number = 0	
		name = ""

def Main(): 
		# Creating an object of the MyClass. Here, 'me' is the object 
		me = MyClass() 

		# Accessing the attributes of MyClass using the dot(.) operator 
		me.number = 2019	
		me.name = "MSOIS"

		# str is an build-in function that creates an string 
		print(me.name + " " + str(me.number)) 
	
# telling python that there is main in the program. 
if __name__=='__main__': 
		Main() 
-------------------------------------------------------------
# Create a class named Person, use the __init__() function 
#to assign values for name and age:
#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age
#
#p1 = Person("Maipal", 2020)
#
#print(p1.name)
#print(p1.age)
#---------------------------------------------------------------
## A Python program to demonstrate working of class methods 
#
#class Vector: 
#		x = 0.0
#		y = 0.0
#
#		# Creating a method named Coordinates 
#		def Coordinates(self, x, y):	 
#				self.x = x 
#				self.y = y 
#
#def Main(): 
#		# vec is an object of class Vector 
#		vec = Vector() 
#		
#		# Passing values to the function Coordinates 
#		# by using dot(.) operator. 
#		vec.Coordinates(100, 250)	 
#		print("X: " + str(vec.x) + ", Y: " + str(vec.y)) 
#
#if __name__=='__main__': 
#		Main() 
#---------------------------------------------------------------
#The class attribute "a" is the same for all instances, 
#in our example "x" and "y". 
# We see that we can access a class attribute via an instance 
#or via the class name.

class A:
    a = "I am a class attribute!"

x = A()
y = A()
print("Displaying 'a' using instance attriute 'x' is:")
print(x.a)  #'I am a class attribute!'
print("Displaying 'a' using instance attriute 'y' is:")
print(y.a)   #'I am a class attribute!'
print("Displaying 'a' using class attriute is:")
print(A.a)   #'I am a class attribute!'
#---------------------------------------------------------------

# If you want to change a class attribute, 
#you have to do it with the notation ClassName. orAttributeName. 
#Otherwise, you will create a new instance variable.

class A:
    a = "I am a class attribute!"

x = A()
y = A()
print("Displaying 'a' using instance attriute 'x' is:")
print(x.a)  #'I am a class attribute!'
print("Changing the Instance attribute of X" )
x.a = "This creates a new instance attribute for x!"
print(x.a) #"This creates a new instance attribute for x!"
print("Displaying 'a' using instance attriute 'y' is:")
print(y.a) #'I am a class attribute!'
print("Displaying 'a' using class attriute is:")
print(A.a)   #'I am a class attribute!'
print("Changing the Class attribute of a")
A.a = "This is changing the class attribute 'a'!"
print(A.a) #"This is changing the class attribute 'a'!"
print(y.a) #"This is changing the class attribute 'a'!"
# But x.a is still the previously created instance variable:
print(x.a) #'This creates a new instance attribute for x!'

#--------------------------------------------------------------------
