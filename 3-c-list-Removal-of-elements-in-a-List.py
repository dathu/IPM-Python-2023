# Python program to demonstrate Removal of elements in a List 

# Creating a List 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 

# Removing elements from List using Remove() method 
List.remove(5) # 5 is an item(values) not index
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 

# Removing elements from List using iterator method (2,3,4)
for i in range(2, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

# Removing element from the Set using the pop() method:Removes and returns an element at the given index
List.pop() 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a specific location from the Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 
