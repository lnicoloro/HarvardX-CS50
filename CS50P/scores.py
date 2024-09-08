scores = [72, 73, 33]

average = sum(scores) / len(scores)

print(average)


from cs50 import get_int

scores = []

for i in range(3):
    score = get_int('Score: ')
    # scores.append(score)
    score += [score]            ## can conncatonate lists

average = sum(scores) / len(scores)

print(f'{average}')

