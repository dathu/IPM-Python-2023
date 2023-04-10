# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:21:44 2019

@author: dathe
"""
#creating a simple class, its instance and accessing the attributes of a class
class Hello:
    a =5
    print("Welcome to MSOIS")

x = Hello()
print(x.a) #all attributes are public

#--------------------------------------------------------------------------

"""We Shall have a class defined for vehicles. 
#Create two new vehicles called car1 and car2. 
Set car1 to be a red hatchback worth Rs. 6,00,000.00 with a name of Tatanexon, and 
car2 to be a blue van named Jeep worth RS. 10,00,000.00."""

# define the Vehicle class
class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 0.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Tatanexon"
car1.color = "red"
car1.kind = "hatchback"
car1.value = 600000.00

car2 = Vehicle()
car2.name = "Jeep"
car2.color = "blue"
car2.kind = "van"
car2.value = 1000000.00

# test code
print(car1.description())
print(car2.description())

#---------------------------------------------------------------------

# __init__method example:

class car:
  "A simple class for cars"
 
  #Constructor to initialize
  def __init__(self,company,color):
    self.company = company
    self.color = color

  #function to print car company and color
  def display(self):
    print ('This is a', self.color, self.company)

obj = car('TATA- Harrier','Red')
obj.display()

#-------------------------------------------------------------------------

#Deleting an Object Reference

class car:
  "A simple class for cars"
 
  #Constructor to initialize
  def __init__(self,company,color):
    self.company = company
    self.color = color

  #function to print car company and color
  def display(self):
    print ('This is a', self.color, self.company)

obj = car('Hyundai-Venue','Black')
obj.display()

del obj  #this will delete the object obj
obj.display()

#-----------------------------------------------------------------------------

#Making attributes private

class Car:
  "A simple class for cars"
 
  #Constructor to initialize
  def __init__(self,company,color):
    self.company = company
    self.__color = color  #making color private

  #function to print car company and color
  def display(self):
    print ('This is a', self.__color, self.company)

#creating the object
obj = Car('BMW','Black')
print (obj.company)  #company is not private
print (obj.__color)  #color is private  

#-------------------------------------------------------------------------

# Python Builtin Classes

class Car:
  "A simple class for cars"
 
  #Constructor to initialize
  def __init__(self,company,color):
    self.company = company
    self.color = color  #making color private

  #function to print car company and color
  def display(self):
    print ('This is a', self.color, self.company)

print ('car.__name__ = ',car.__name__)
print ('car.__doc__ = ',car.__doc__)
print ('car.__module__ = ',car.__module__)
print ('car.__dict__ = ',car.__dict__)

#-------------------------------------------------------------------------