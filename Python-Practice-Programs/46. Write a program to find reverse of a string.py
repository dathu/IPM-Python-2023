'''
Description:
Description is mentioned below with the help of comments in roman urdu.
'''

# 1st Method:

# text = input('Enter String to find its reverse: ').casefold()
# print('The reverse of a string is',text[-1::-1])

# 2nd method:

# text = 'ram' 
# 2 se start lega or -1 tak jaiga matlb -1 se ek ziyada matlb 0 tak jaiga
# or har dafa ek ka decrement hoga.
# i ki value jab -1 to program terminate because ek ziyada tak chalta hai or 0 tak jaiga isliye
# -1 or -1 clash or program terminate.
# for i in range((len(text)-1), -1, -1):
#     print(text[i], end='')

# 3rd method:

# text = 'ram'
# print(text[-1:-4:-1])