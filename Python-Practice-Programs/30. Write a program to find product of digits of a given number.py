"""
Description:
Same logic like Program#25.
"""

no = int(input('Enter Number to find product of digits of a number: '))
product = 1 # for sum we initialize sum to 0 but for product we initialize product to 1.
while no > 0:
    product = product * (no % 10)
    no = no // 10
print('Product of digits of a number =', product)
