"""
Write a program to accept total sales amount and find the profit amount @ 5%.

Description:

lets say total sales is 50k so we have to find profit which is 5% of the total sales.
if a person sales 50k a day then it means 5 percent of profit is 50,000 * 5/100 = 25,00.
so 25,00 is the profit he gains if he sales 50,000 a day.
"""

totalSalesperDay = int(input('Enter total sales per day: '))

proFIT = int(input('Enter a profit percentage which you want from total sales per day: '))

profitAmount = totalSalesperDay * (proFIT / 100)

print('Total profit if the total sales per day is', totalSalesperDay, 'is equal to', profitAmount)