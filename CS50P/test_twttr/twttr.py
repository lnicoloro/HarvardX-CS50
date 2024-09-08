def main():
    word = input('Input: ')
    print(shorten(word))


def shorten(word):
    no_vowels = ''
    for i in word:
        if i.lower() != 'a' and i.lower() != 'e' and i.lower() != 'i' and i.lower() != 'o' and i.lower() != 'u':
            no_vowels += i
    return no_vowels


if __name__ == "__main__":
    main()


