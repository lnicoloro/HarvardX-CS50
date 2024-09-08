import random


def main():
    level = get_level()
    score = game(level)
    print(f'Score: {score}')




def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
    else:
        raise ValueError



def round(x, y):
    tries = 0
    while tries <=2:
        try:
            answer = int(input(f'{x} + {y} = '))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print('EEE')
        except:
            tries += 1
            print('EEE')
    print(f'{x} + {y} = {x + y}')
    return False


def game(level):
    rounds = 0
    score = 0
    while rounds <= 9:
        x, y = generate_integer(level)
        guess = round(x, y)
        if guess == True:
            score += 1
        rounds += 1
    return score



if __name__ == "__main__":
    main()