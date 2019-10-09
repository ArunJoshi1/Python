import math
weight = int(input("weigth: "))
uint = input('kg or lbs(k or l) :').lower()

if uint == 'l':
    converted = weight*0.45
    print(f'your weight is  {math.ceil(converted)} kg')
else:
    converted = weight//(0.45)
    print(f'your weight is {math.ceil(converted)} lbs')
