vowels = input('Input: ')

no_vowels = ''

for i in vowels:
    if i.lower() != 'a' and i.lower() != 'e' and i.lower() != 'i' and i.lower() != 'o' and i.lower() != 'u':
        no_vowels += i

print(no_vowels)
