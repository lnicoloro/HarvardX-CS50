import random

while True:
    try:
        level = input('Level: ')
        level = int(level)
        if level <= 0:
            pass
        else:
            break
    except ValueError:
        pass

value = random.randrange(1,level+1)

while True:
    try:
        guess = input('Guess: ')
        guess = int(guess)
        if guess > 0:
            if guess < value:
                print('Too small!')
                pass
            elif guess > value:
                print('Too large!')
                pass
            else:
                print('Just right!')
                break
        else:
            pass
    except ValueError:
        pass