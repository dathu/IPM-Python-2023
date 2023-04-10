# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:11:10 2019

@author: dathe
"""
'''show this Exception error tree
https://docs.python.org/2/library/exceptions.html#exception-hierarchys'''


#Syntax Error
#print( 0 / 0 ))

#------------------------------------------------------------------------------
#syntactically correct Python code results in an error

#print( 0 / 0) #ZeroDivisionError: division by zero
#------------------------------------------------------------------------------

#Raiseing an Exception

#x = input('Enter the value for x:')
#y = int(x)
#if y > 5:
#    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
#else:
#    print('No Exception as x is less than 5')

#------------------------------------------------------------------------------
#Try Catch Exception 1


#Total_Marks = int(input("Enter Total Marks Scored: "))
#Num_of_Sections = int(input("Enter Num of Sections: "))
#Average = 0
#try:
#    Average = int(Total_Marks/Num_of_Sections)
#except ZeroDivisionError:
#    print("There has to be atleast 1 or more than 1 sections.")
#print("Average marks scored per section is: ",Average)

#----------------------------------------------------------------------------
#Try Catch Exception 2

# import module sys to get the type of exception
#import sys
#
#mylist = ['a', 0, 2]
#
#for entry in mylist:
#    try:
#        print("The entry is", entry)
#        r = 1/int(entry)
#        break
#    except:
#        print("Oops!",sys.exc_info()[0],"occured.")
#        print("Next entry.")
#        print()
#print("The reciprocal of",entry,"is",r)

#-------------------------------------------------------------------------

#File Not found Error and Try, except


#try:
#    f = open("demofile.txt")
#except:
#    print("File not found. Create file before opening it." )

#-------------------------------------------------------------------------------
#Try Catch Else Exception (show code)

#while True:
#    try:
#        x = int(input("Please enter a number: "))
#    except ValueError:
#        print("Please enter a valid number!")
#    else:
#        print("%s squared is %s" % (x, x**2))
    
#        
#------------------------------------------------------------------------
  
#Try Except and Finqlly

#file = open('test1.txt', 'r') #change w to r for IOError 
#
#try:
#    file.write("Testing.")
#    print("Writing to file.")
#except IOError:
#    print("Could not write to file.")
#else:
#    print("Write successful.")
#finally:
#    file.close()
#    print("File closed.")

#--------------------------------------------------------------------        