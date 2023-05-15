"""
Description:
Casefold method returns a string where all the characters are lower case.
isPalindrome function simply check whether the string is palindrome or not.
This function also executes the correct conditional statement for int values.
"""

def isPalindrome(sTr):
    if sTr[-1::-1] == sTr:
        print('The String is a palindrome string.')
    else:
        print('The String is not palindrome. ')
text = input('Enter text to check whether it is palindrome or not: ').casefold()
isPalindrome(text)