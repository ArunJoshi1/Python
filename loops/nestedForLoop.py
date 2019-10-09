for row in range(0,5):
    for col in range(0,row):
        print('*',end=" ")
    print("")


numbers=[5,2,5,2,2]

for row in numbers:
    for count in range(0,row):
        print('X',end='')
    print("")