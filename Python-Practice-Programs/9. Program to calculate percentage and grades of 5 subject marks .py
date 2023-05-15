"""
Write a program to accept marks of 5 subjects and find total marks and percentage assumimg full marks as
100 in each subject.
"""

markOfsubj1 = int(input('Enter marks of subject#1: '))
markOfsubj2 = int(input('Enter marks of subject#2: '))
markOfsubj3 = int(input('Enter marks of subject#3: '))
markOfsubj4 = int(input('Enter marks of subject#4: '))
markOfsubj5 = int(input('Enter marks of subject#5: '))

obtainMarks = markOfsubj1 + markOfsubj2 + markOfsubj3 + markOfsubj4 + markOfsubj5
totalMarks = 500

percentage = (obtainMarks / totalMarks) * 100

print('The total obtain marks is:', obtainMarks, '\nThe percentage is:', percentage,'%')

"""
You can also calculate grades with the help of percentage like if percentage >= 80 then display A-grade.
if percentage >= 60 then display B-grade. if percentage >= 40 then display C-grade and if
percentage < 40 then display D-grade or you can put this condition into else block as well.
"""

