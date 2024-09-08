# TODO


text = input('Text: ')

characters = 0
words = 1
sentences = 0

for i in text:
    if i.isalpha():
        characters += 1

    if i == " ":
        words += 1

    if i == "." or i == "?" or i == "!":
        sentences += 1


L = characters / words * 100

S = sentences / words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)


if index < 1:
    print('Before Grade 1')

elif index >= 16:
    print('Grade 16+')

else:
    print(f"Grade {index}")


