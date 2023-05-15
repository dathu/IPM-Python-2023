"""
Question: Write a program to accept electricity unit consumption and calculate total price at the rate of
 5 rs unit. Give a discount of 10% on all over bill.
"""

"""
Description:

5 rupee per unit.
if user enters 200 units then it means 200*5 = 1000(total price), it is the price that you have to
pay means 1000 Rs of elctricity is used.
"""

unit = int(input('Enter units: '))
rupeePerUnit = 5
totalPrice = unit * rupeePerUnit
print('Total price is:', totalPrice)
priceAfterdiscount = totalPrice * 0.90
print('Price after 10% of discount is:', priceAfterdiscount)
