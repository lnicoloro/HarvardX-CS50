word = set()        ##set is a collection of values with no duplicates equivalent of a hash table

def check(word):
    if word.lower() in word:
        return True
    else:
        return False:

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip()        ##removes the "\n" at the end of a line
        words.add(line)
    close(file)
    return True

def size():
    return len(words)

def unload():
    return True     ##the unloading and assigning of memory is done automatically