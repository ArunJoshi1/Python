import random

ran = random.randrange(1, 10, 1);
guess_count = 0
guess_limit = 3
print(f'Enter Number B/w 0 and 10')
while guess_count != guess_limit:
    guess_count += 1
    number = int(input("Enter a Number: "))

    if ran == number:
        print(f'you won..Hurray {ran} equals to {number}')
        break
    else:
        print(f'guess count remain {guess_limit - guess_count}')
    if guess_count == guess_limit:
        print(f'sorry you failed. random number is {ran}')
