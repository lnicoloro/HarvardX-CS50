from collections import OrderedDict
dict = {}

while True:
    try:
        item = input("").upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    except EOFError:
        dict = OrderedDict(sorted(dict.items()))
        for item in dict:
            print(dict[item], item)
        break