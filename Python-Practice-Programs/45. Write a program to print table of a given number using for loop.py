while True:
    no = int(input('Enter Number to find its table: '))
    for i in range(1, 11):
        print(f'{no} x {i} =', no * i)