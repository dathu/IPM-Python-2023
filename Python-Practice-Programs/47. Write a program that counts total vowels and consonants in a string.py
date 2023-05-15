'''
Casefold is basically a method that turns the string into lower case format.
'''

text = input('Enter string: ')
vowel = 0
consonant = 0
for i in range(0, len(text)):
    if text[i] != '':
        if (text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u'
            or text[i] == 'A' or text[i] == 'E' or text[i] == 'I' or text[i] == 'O' or text[i] == 'U'):
            vowel += 1
        else:
            consonant += 1
print('Total Vowels =', vowel)
print('Total Consonant\'s =', consonant)
