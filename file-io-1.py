#Create a file by name demofile.txt in the same folder as other
#python codes.
# Here open() is a builtin function

#Reading Complete File Content

print("Reading Complete File Content:\n")
f = open("demofile.txt") # their should be a file by this name
#f = open("demofile.txt", "rt")
print(f.read())
print("#--------------------------------------")

#f = open("myfile.txt", "x") #Create a file called "myfile.txt"
#f = open("myfile.txt", "w") #Create a new file if it does not exist
f.close()
#---------------------------------------------------

#Reading Only Parts of the File

print("Reading Only Parts of the File Content:\n")
f = open("demofile.txt", "r")
print(f.read(10))  # 10 is no of characters
print("#--------------------------------------")
f.close()
#---------------------------------------------------

#Reading Line

print("Reading Lines of the File Content:\n")
f = open("demofile.txt", "r")
print(f.readline())
print("#--------------------------------------")
f.close()
#---------------------------------------------------

#looping through the lines of the file

print("Looping Through the Lines of the File:\n")
f = open("demofile.txt", "r")
for x in f:
  print(x)
print("#--------------------------------------")
f.close()
#---------------------------------------------------






#---------------------------------------------------
# Remove the file "demofile1.txt"

##import os
##print("Remove the file demofile1.txt:\n")
##os.remove("demofile1.txt")
##print(" file demofile1.txt Deleted Successfully check the folder\n")
##print("#--------------------------------------")

#---------------------------------------------------

#To avoid getting an error,
#you might want to check if the file exist before you try to delete it

##import os
##if os.path.exists("demofile1.txt"):
##  os.remove("demofile1.txt")
##else:
##  print("The file does not exist")
##
##print("#--------------------------------------")

#---------------------------------------------------














#overwrite any existing content

##print("overwrite any existing content:\n")
##f = open("demofile.txt", "w")
##f.write("Woops! I have deleted the content!")

#---------------------------------------------------
###Write to an Existing File
##
##print("Write to an Existing File:\n")
##f = open("demofile.txt", "a")
##f.write("Now the file has one more line!:")
###print(f.read())
##print("#--------------------------------------")

#---------------------------------------------------

